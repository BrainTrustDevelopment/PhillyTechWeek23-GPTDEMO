import openai
import os

# Set your OpenAI API key
openai.api_key = os.environ["OPENAI_API_KEY"]

# Set the prompt you want to send to GPT-3
messages=[
    {
        "role": "user", 
        "content":  "Hello, world!"
    }
]

# Send the prompt to GPT-3 and receive a response
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", 
    messages=messages
)

output = response.choices[0].message.content

# Print the response text
print(output)
