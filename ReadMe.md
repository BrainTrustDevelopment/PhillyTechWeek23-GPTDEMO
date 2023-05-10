# GPT , Python, and Me 
## Philly Tech Week 2023

## Link to Repo
![](./frame.png)

## Getting Started

1. Open open a new terminal window or gitbash.
3. In the terminal window, type `export OPENAI_API_KEY=your-api-key-here` and press Enter. Replace "your-api-key-here" with your actual OpenAI API key.
4. To confirm that the environment variable has been set correctly, type `echo $OPENAI_API_KEY` and press Enter. You should see your API key printed in the terminal.

## 01-Basic

**Description:** This code snippet demonstrates how to use the OpenAI API with GPT-3.5-turbo for a chat-based interaction. The script follows these steps:

1. Import the required libraries (openai and os).
2. Set the OpenAI API key by retrieving it from the environment variable "OPENAI_API_KEY".
3. Define a list called "messages" that contains a single message object with a "user" role and the content "Hello, world!".
4. Send the "messages" list to the GPT-3.5-turbo model using the OpenAI ChatCompletion API.
5. Extract the generated response from GPT-3.5-turbo and store it in the variable "output".
6. Print the response text (output) to the console.

## 02-JokeGPT

**Description:** This code snippet demonstrates how to use the OpenAI API with GPT-3.5-turbo to generate an AI-themed joke. The script follows these steps:

1. Import the required libraries (openai and os).
2. Set the OpenAI API key by retrieving it from the environment variable "OPENAI_API_KEY".
3. Define a function called "get_joke()" that performs the following actions:
    a. Set a prompt asking GPT-3 to generate an AI-themed joke for a developer starting an AI workshop.
    b. Create a list called "messages" that contains a single message object with a "user" role and the content set to the prompt.
    c. Send the "messages" list to the GPT-3.5-turbo model using the OpenAI ChatCompletion API.
    d. Extract the generated joke from GPT-3.5-turbo and store it in the variable "joke".
    e. Return the joke.
4. In the main script, if the script is being run as the main program, execute the following actions:
    a. Print "Asking GPT-3 for a joke..." to the console.
    b. Call the "get_joke()" function to retrieve a joke from GPT-3.5-turbo.
    c. Print "Here's a joke from GPT-3:" and the generated joke to the console.

## 03-SimpleChat

**Description:** This code snippet demonstrates how to use the OpenAI API with GPT-3.5-turbo to generate three ideas for apps that can be built using OpenAI APIs. The script follows these steps:

1. Import the required libraries (openai and os).
2. Set the OpenAI API key by retrieving it from the environment variable "OPENAI_API_KEY".
3. Define a prompt asking GPT-3 to generate three ideas for apps that can be built using OpenAI APIs.
4. Create a list called "messages" that contains a single message object with a "user" role and the content set to the prompt.
5. Send the "messages" list to the GPT-3.5-turbo model using the OpenAI ChatCompletion API.
6. Extract the generated response from GPT-3.5-turbo.
7. Print the response text to the console.

## 04-BrainStrom

**Description:** This code snippet demonstrates how to use the OpenAI API with GPT-3.5-turbo to generate three ideas for apps that can be built using OpenAI APIs. The script follows these steps:

1. Import the required libraries (openai and os).
2. Set the OpenAI API key by retrieving it from the environment variable "OPENAI_API_KEY".
3. Define a prompt asking GPT-3 to generate three ideas for apps that can be built using OpenAI APIs.
4. Create a list called "messages" that contains a single message object with a "user" role and the content set to the prompt.
5. Send the "messages" list to the GPT-3.5-turbo model using the OpenAI ChatCompletion API.
6. Extract the generated response from GPT-3.5-turbo.
7. Print the response text to the console.

## 05-WebUi


**Description:** This code snippet demonstrates how to create a chatbot using the OpenAI API with GPT-3.5-turbo and Gradio, which provides the worst dating advice ever. The script follows these steps:

1. Import the required libraries (openai, gradio, and os).
2. Set the OpenAI API key by retrieving it from the environment variable "OPENAI_API_KEY".
3. Define an initial message with the role "system" that instructs GPT-3 to act as a friend who gives the worst PG-rated dating advice.
4. Create a function called "CustomChatGPT" that takes a user_input parameter and performs the following actions:
    a. Append the user_input message to the existing "messages" list with the role "user".
    b. Send the "messages" list to the GPT-3.5-turbo model using the OpenAI ChatCompletion API.
    c. Extract the generated response from GPT-3.5-turbo, and store it in the variable "ChatGPT_reply".
    d. Append the ChatGPT_reply message to the "messages" list with the role "assistant".
    e. Return the ChatGPT_reply.
5. Create a Gradio interface called "demo" with the function "CustomChatGPT", a single text input, a single text output, and a title "Bad Dating Advice Pro".
6. Launch the Gradio interface with the "share" parameter set to True, enabling it to be shared with others.

## 06-TeachingAssistant

**Description:** This code snippet demonstrates how to use the OpenAI API with GPT-3.5-turbo to evaluate a candidate's response to a technical interview question based on a predefined rubric. The script follows these steps:

1. Import the required libraries (openai and os).
2. Set the OpenAI API key by retrieving it from the environment variable "OPENAI_API_KEY".
3. Define a technical interview question about polymorphism in object-oriented programming.
4. Create a function called "generate_gpt3_response()" that takes two parameters: "question" and "answer". Inside this function:
    a. Define a prompt that instructs GPT-3 to evaluate the applicant's response based on the given rubric.
    b. Create a list called "messages" that contains a single message object with a "system" role and the content set to the prompt.
    c. Send the "messages" list to the GPT-3.5-turbo model using the OpenAI ChatCompletion API.
    d. Extract the generated evaluation response from GPT-3.5-turbo and store it in the variable "result".
    e. Return the result.
5. In the main script, if the script is being run as the main program, execute the following actions:
    a. Print the question to the console.
    b. Prompt the user to input their answer.
    c. Call the "generate_gpt3_response()" function with the question and user's answer as arguments.
    d. Print the evaluation score generated by GPT-3.5-turbo to the console.

**Question:** 
Can you explain the concept of polymorphism in object-oriented programming, provide an example of its use, and discuss its benefits in software development?

**Response 1 (Amazing):**
Polymorphism is a key concept in object-oriented programming that allows objects of different classes to be treated as objects of a common superclass. It enables a single interface to represent different data types and perform specific actions based on the data type. This promotes code reusability, modularity, and scalability in software development.

For example, consider a drawing application supporting multiple shapes like circles, rectangles, and triangles. We could create a base class 'Shape' with a method 'draw' and subclasses like 'Circle', 'Rectangle', and 'Triangle' that inherit from 'Shape' and override 'draw'. Using polymorphism, we can create a list of 'Shape' objects and call 'draw' on each, executing the correct method for each shape without knowing its specific type. This improves code maintainability and simplifies the overall structure.


**Response 2 (Poor):**
Polymorphism is when you use, like, one thing to do different stuff in code. It's helpful, I guess.

For example, you have shapes or something and they draw differently, so you use polymorphism. It makes things easier to change, maybe.

## Further Learning 

[Free OpenAi Class](https://learn.deeplearning.ai/)

