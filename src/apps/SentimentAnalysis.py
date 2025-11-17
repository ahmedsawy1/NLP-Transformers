from transformers import pipeline
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
import torch

pipe = pipeline(
    "text-classification", model="distilbert-base-uncased-finetuned-sst-2-english"
)
# pipe = pipeline("text-classification", model="ProsusAI/finbert")
# pipe = pipeline("text-classification", model="tabularisai/multilingual-sentiment-analysis")


def analyze_sentiment(text: str) -> dict:
    result = pipe(text)
    print("text: ", text)
    print("result: ", result)
    return result
