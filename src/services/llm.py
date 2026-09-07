import os

from dotenv import load_dotenv
from groq import Groq


load_dotenv()


def get_client() -> Groq:
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError("GROQ_API_KEY is not configured.")

    return Groq(api_key=api_key)


def generate_response(question: str, context: str) -> str:
    client = get_client()

    prompt = f"""
You are a customer support assistant.

Answer the customer's question using ONLY the information provided
in the knowledge base.

If the knowledge base does not contain enough information to answer
the question, say that you do not have enough information.

Knowledge base:
{context}

Customer question:
{question}
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful and accurate customer support assistant.",
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        temperature=0,
    )

    return response.choices[0].message.content
