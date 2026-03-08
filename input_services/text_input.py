from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

user_input = input("Type your idea:\n")

llm = ChatGroq(
    groq_api_key=groq_api_key,
    model_name="llama-3.1-8b-instant"
)

def script_enhancer(user_input):
    # Generate a response
    response = llm.invoke(
        f"""
            Convert the following idea into a natural spoken script for a talking avatar.

            Rules:
            - Write only ONE continuous paragraph.
            - No headings, bullet points, markdown, or formatting.
            - Do not explain anything.
            - Do not add introductions like "Here is the script".
            - The output should sound natural when spoken aloud.
            - Length: 80–120 words.

            User input:
            {user_input}
        """
    )
    
    main_content = response.content
    return main_content

script = script_enhancer(user_input)

print(script) # <<-- Remove this