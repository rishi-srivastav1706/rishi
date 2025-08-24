import os
from openai import OpenAI

token ="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"
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-5"
a = 7
client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "",
        },
        {
            "role": "user",
            "content": "What is the capital of France?",
        }
    ],
    model=model
)
     
print(response.choices[0].message.content)

