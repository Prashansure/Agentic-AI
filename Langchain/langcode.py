"""
==========================================================
LangChain for AI Agents — Gemini Companion Code
==========================================================

Demonstrates:
- ReAct-style agent behavior
- Tool calling
- Multiple tool calls
- Error handling
- LangChain create_agent()
- Google Gemini as the LLM

Prerequisites:
    pip install -U langchain langgraph langchain-google-genai python-dotenv

.env:
    GOOGLE_API_KEY=your-gemini-api-key
==========================================================
"""

# -------------------------------------------------------
# STEP 0: Load environment variables
# -------------------------------------------------------

import os
import math
from dotenv import load_dotenv

load_dotenv()

if not os.getenv("GEMINI_API_KEY"):
    raise ValueError("GEMINI_API_KEY not found in .env")


# -------------------------------------------------------
# STEP 1: Initialize Gemini
# -------------------------------------------------------

from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    temperature=0,
)


# -------------------------------------------------------
# STEP 2: Define Tools
# -------------------------------------------------------

from langchain_core.tools import tool


@tool
def add(a: float, b: float) -> float:
    """
    Add two numbers together.
    Use this tool when the user asks for addition.
    """
    return a + b


@tool
def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers together.
    Use this tool when the user asks for multiplication.
    """
    return a * b


@tool
def divide(a: float, b: float) -> str:
    """
    Divide the first number by the second.
    Returns an error if dividing by zero.
    """
    if b == 0:
        return "Error: Cannot divide by zero"

    return str(a / b)


@tool
def square_root(number: float) -> str:
    """
    Calculate the square root of a number.
    Returns an error for negative numbers.
    """
    if number < 0:
        return "Error: Cannot take square root of a negative number"

    return str(math.sqrt(number))


tools = [
    add,
    multiply,
    divide,
    square_root,
]


# -------------------------------------------------------
# STEP 3: Show Available Tools
# -------------------------------------------------------

print("=== Available Tools ===")

for tool_item in tools:
    print(f"  • {tool_item.name}: {tool_item.description}")

print()


# -------------------------------------------------------
# STEP 4: Create Agent
# -------------------------------------------------------

from langchain.agents import create_agent

agent = create_agent(
    model=model,
    tools=tools,
)


# -------------------------------------------------------
# STEP 5: Run Agent
# -------------------------------------------------------

def run_agent(question: str):

    print(f"\n🧑 User: {question}")
    print("-" * 60)

    result = agent.invoke({
        "messages": [
            ("user", question)
        ]
    })

    print("🔎 Agent Execution Trace")
    print("-" * 60)

    step = 1

    for msg in result["messages"]:

        # User message
        if msg.type == "human":

            print(f"{step}. User asked:")
            print(f"   {msg.content}")
            step += 1

        # Agent tool decision
        elif msg.type == "ai" and getattr(msg, "tool_calls", None):

            for tool_call in msg.tool_calls:

                print(f"{step}. Agent decision:")
                print(
                    f"   Tool: {tool_call['name']}"
                )
                print(
                    f"   Input: {tool_call['args']}"
                )

                step += 1

        # Tool result
        elif msg.type == "tool":

            print(f"{step}. Tool observation:")
            print(f"   Result: {msg.content}")

            step += 1

        # Final response
        elif msg.type == "ai" and msg.content:

            print(f"{step}. Final answer:")

            if isinstance(msg.content, str):
                print(f"   {msg.content}")
            else:
                print(f"   {msg.content}")

            step += 1

    print("=" * 60)


# -------------------------------------------------------
# STEP 6: Test Cases
# -------------------------------------------------------

run_agent(
    "What is 42 + 58?"
)

run_agent(
    "What is 15 multiplied by 8, then divided by 3?"
)

run_agent(
    "I have a rectangle with width 12 and height 7. "
    "What is its area, and what is the square root of that area?"
)

run_agent(
    "What is 100 divided by 0?"
)


print("\n✅ Gemini Agent Demo Complete!")