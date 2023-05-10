import openai
import os

# Set up OpenAI API credentials
openai.api_key = os.environ["OPENAI_API_KEY"]

question = "Can you explain the concept of polymorphism in object-oriented programming, provide an example of its use, and discuss its benefits in software development?"

def generate_gpt3_response(question,answer):
    prompt = f"""
        You are a technical hiring manager interviewing college graduate's response for an entry-level developer position.  You would like to evaluate their response and evaluated it based of the following rubric:

        1. Clarity (0-4 points)
        2. Accuracy (0-4 points)
        3. Relevance (0-4 points)
        4. Examples (0-4 points)
        5. Organization & Structure (0-4 points)
        6. Creativity & Critical Thinking (0-4 points)

        The question will be a technical question in the domain of software engineering and programming. An example question is like the one in between the triple hash marks

        ###Can you describe what is meant by the decomposition estimation technique?###

        Typical student response will be like the one contained in between the triple percent signs

        %%%Big-O notation is a concept used to describe the performance of an algorithm. It helps in determining the worst-case scenario in terms of time complexity, which is the maximum time an algorithm may take to execute. The notation uses 'O' followed by a function that represents the growth of the algorithm's runtime based on its input size, e.g., O(n) for linear time complexity.%%% 

        Typical response below:

        {{
            "response": {{
                "Clarity": {{
                    "Score": 4
                }},
                "Accuracy": {{
                    "Score": 4
                }},
                "Relevance": {{
                    "Score": 4
                }},
                "Examples": {{
                    "Score": 3,
                    "Improvements": "Include one or two examples in the response."
                }},
                "Organization_Structure": {{
                    "Score": 4,
                }},
                "Creativity_Critical_Thinking": {{
                    "Score": 2,
                    "Improvements": "Explore more advanced topics or potential limitations or drawbacks of Big-O notation to enhance the response."
                }},
                "Total_Score": 21
            }}
        }}

        The actual question will be contained in between the triple dollar signs bellow:


        $$${question}$$$

        The applicants response is below in between the triple asterisk marks:

        ***{answer}***
        """

    messages=[
        {
            'role':'system',
            'content':prompt
        }
    ]

    # Send the prompt to GPT-3 and receive a response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=messages
    )

    result = response.choices[0].message.content
    return result

if __name__ == "__main__":
    print(f"""Question: {question}""")
    print("Please Answer:")
    answer = input()
    score = generate_gpt3_response(question,answer)
    print(score)