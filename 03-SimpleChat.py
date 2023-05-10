import openai
import os

# Set up OpenAI API credentials
openai.api_key = os.environ["OPENAI_API_KEY"]
prompt = "Give me 3 ideas for apps I could build with openai apis"

messages=[
    {
        "role": "user", 
        "content": prompt
    }
]

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", 
    messages=messages
)

print(response.choices[0].message.content)