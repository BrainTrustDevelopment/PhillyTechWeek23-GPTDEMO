# Link to Repo
![](./frame.png)

# Further Learning 

[Free OpenAi Class](https://learn.deeplearning.ai/)

# Getting Started

1. Open your Visual Studio Code project and create a new Python file or open an existing one.
2. Click on the "Terminal" menu and select "New Terminal" to open a new terminal window.
3. In the terminal window, type `export OPENAI_API_KEY=your-api-key-here` and press Enter. Replace "your-api-key-here" with your actual OpenAI API key.
4. To confirm that the environment variable has been set correctly, type `echo $OPENAI_API_KEY` and press Enter. You should see your API key printed in the terminal.
5. Now you can use the `os` module in Python to retrieve your API key from the environment. Here's an example:

```python
import os
import openai

# Retrieve your OpenAI API key from the environment
openai.api_key = os.environ["OPENAI_API_KEY"]

# Use the OpenAI API as usual
response = openai.Completion.create(...)
```

That's it! With these instructions, you can securely store your OpenAI API key as an environment variable and use it in your Python scripts in Visual Studio Code.

## Teaching Assistant
Question: 
Can you explain the concept of Unit Testing, its importance in software development, and provide an example of how you would write a JUnit test case in Java for a given method?

Response 1 (Amazing):
Unit Testing is a level of software testing where individual units or components of a software are tested in isolation. It helps us validate that each unit of the software performs as expected, allowing us to catch bugs early in the development process, and increasing code maintainability, readability, and reusability. Unit Testing is crucial to maintain high software quality and can save time and resources in the long run.

In Java, JUnit is a popular testing framework for writing and running unit tests. For example, if we have a method `public int add(int a, int b)` in a class `Calculator`, we can write a JUnit test case. We would import the necessary JUnit classes, create a test class `CalculatorTest`, and define a test method `testAdd()` annotated with `@Test`. We then instantiate the `Calculator` class, call the `add()` method, and use `assertEquals()` to check if the result is as expected.

Response 2 (Good):
Unit Testing is the process of testing individual units or components of a software to ensure they are working as expected. It's important for catching bugs early, maintaining code quality, and ensuring the software is reliable.

In Java, JUnit is a widely used framework for writing unit tests. For example, if there's a method `public int add(int a, int b)` in a class `Calculator`, a JUnit test case for this method can be written. We would import the necessary JUnit classes, create a test class, and use the `@Test` annotation to define a test method. We then create an instance of the `Calculator` class and use `assertEquals()` to check if the result is correct.

Response 3 (Poor):
Unit Testing is when you test the code. It's important because you want to make sure your code works. In Java, you can use JUnit to test your code. For example, if you have an `add()` method, you can write a test. In this example, I created a test class and a test method, then printed the result of the `add()` method to check if it's correct.
