from groq import Groq
import ast
from os import getenv
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=getenv("GROQ_API_KEY"))
def callGroq(text):
    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
            "role": "system",
            "content": """"Convert the input text into a list of independent, 1-2 sentence flashcard facts. Rules: 1. Self-Containment: Every element must be fully understandable alone. Replace pronouns (it, they, these) and references (the following, this goal) with the specific subject/noun. 2. Contextual Injection: If a sentence refers to a group (e.g., 'these 4 layers'), explicitly name or define them within that sentence. 3. Expansion: Convert fragments (e.g., 'Purpose:') into complete definitions (e.g., 'The purpose of the operating system is...'). 4. Detail: Add necessary context to ensure each element is a complete educational unit. 5. No Sequential Logic: Do not expect the user to connect dots between items; treat each as a standalone fact. Output Format: A Python-style list of strings: ['fact1', 'fact2', ...]. Write the output in the language same as the original string input. Only include text and UTF-8 characters in the response, if anything could result an error from your side then jump over that element and skip to the next one to prevent any errors."""
        },
        {
            "role": "user",
            "content": text
        }
        ],
        temperature=1,
        max_completion_tokens=8192,
        top_p=1,
        reasoning_effort="medium",
        stream=False,
        stop=None
    )

    try:
        string_list = ast.literal_eval(completion.choices[0].message.content)
        
        if isinstance(string_list, list) and all(isinstance(item, str) for item in string_list):
            print("Safe conversion successful!")
        else:
            print("The input is not a list of strings.")
            string_list = []
    except (ValueError, SyntaxError):
        print("Invalid input!")
        string_list = []

    return string_list
