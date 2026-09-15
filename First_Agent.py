"""
Tool-Using AI Agent with Gemini

This agent has three tools:
- add()
- multiply()
- perimeter()

Gemini decides which tool to use based on the user's request.

Install:
pip install google-genai python-dotenv
"""

import os
from dotenv import load_dotenv
from google import genai

# Load API key from .env
load_dotenv()

# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


def perimeter(length: float, width: float) -> float:
    """Find the perimeter of a rectangle."""
    return 2 * (length + width)


# Make the functions available as tools
tools = [add, multiply, perimeter]


# Get the user's request
user_input = input("What do you want to calculate? ")


# Let Gemini choose the appropriate tool
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=user_input,
    config={
        "tools": tools,
        "system_instruction": (
            "You are a calculator agent. "
            "Use the available tools when the user asks "
            "for addition, multiplication, or rectangle perimeter."
        )
    }
)


print("\n" + "=" * 50)
print("RESULT")
print("=" * 50)
print(response.text)