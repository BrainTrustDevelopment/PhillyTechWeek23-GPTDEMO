import openai
import os

# Set up OpenAI API credentials
openai.api_key = os.environ["OPENAI_API_KEY"]

def get_joke():
    prompt = "You an developer starting a workshop on AI, and you want to start off with a joke to warm up the crowd. Come up with a AI Joke."
    # Set the prompt you want to send to GPT-3
    messages=[
        {
            "role": "user", 
            "content":  prompt
        }
    ]
    # Send the prompt to GPT-3 and receive a response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=messages
    )

    joke = response.choices[0].message.content
    return joke

if __name__ == "__main__":
    print("Asking GPT-3 for a joke...")
    joke = get_joke()
    print("Here's a joke from GPT-3:")
    print(joke)
