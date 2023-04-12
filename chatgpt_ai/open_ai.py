from dotenv import load_dotenv
import os
import openai

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def chatgpt_response(prompt):
    response = openai.Completion.create(
        model="davinci",
        prompt=[{"role": "user", "text": prompt}],
        max_tokens=200, 
    )
    new_response=response.choices[0]['message']['content']
    
    return response
    