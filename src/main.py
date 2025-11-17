from fastapi import FastAPI
from pydantic import BaseModel
from apps.SentimentAnalysis import analyze_sentiment
from apps.TextSummarizer import summarize_text

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

@app.post("/summarize-text")
def summarize_text_endpoint(request: SentimentRequest):
    result = summarize_text(request.text)
    return {"result": result}
