from fastapi import FastAPI
from pydantic import BaseModel, Field

from src.services.agent import answer_question


app = FastAPI(
    title="AI Customer Support Agent",
    description="API for an AI-powered customer support assistant.",
    version="1.0.0",
)


class ChatRequest(BaseModel):
    message: str = Field(
        min_length=1,
        max_length=500,
    )


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/chat")
def chat(request: ChatRequest):
    answer = answer_question(request.message)

    return {
        "answer": answer
    }