from fastapi import FastAPI
from pydantic import BaseModel
from apps.SentimentAnalysis import analyze_sentiment

app = FastAPI()


class SentimentRequest(BaseModel):
    text: str


@app.get("/health")
def health_check():
    return {"message": "OK"}


@app.post("/analyze-sentiment")
def analyze_sentiment_endpoint(request: SentimentRequest):
    result = analyze_sentiment(request.text)
    return {"result": result}
