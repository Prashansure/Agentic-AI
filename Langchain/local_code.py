from langchain_ollama import ChatOllama

model = ChatOllama(
    model="llama3.2:3b",
    temperature=0
)

response = model.invoke(
    "what is chess,in 2 lines?"
)

print(response.content)