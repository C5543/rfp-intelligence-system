from openai import OpenAI

client = OpenAI()

res = client.embeddings.create(
    model="text-embedding-3-small",
    input="test"
)

print("OK")