from dotenv import load_dotenv
import os
import openai

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def chatgpt_response(prompt):
    response = openai.Completion.create(
        model="davinci",
        prompt=prompt,
        temperature=0.9,
        max_tokens=10, 
    )
    print (response)
    new_response=response.choices[0].message.content
    print(new_response)
    return response
    