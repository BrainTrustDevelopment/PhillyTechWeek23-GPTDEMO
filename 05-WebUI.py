import openai
import gradio
import os

# Set up OpenAI API credentials
openai.api_key = os.environ["OPENAI_API_KEY"]

messages = [{"role": "system", "content": "You are a friend who gives the worst dating advice ever. Everything you say should result in being rejected. Keep everything PG."}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Bad Dating Advice Pro")

demo.launch(share=True)