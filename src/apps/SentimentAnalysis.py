from transformers import pipeline

pipe = pipeline("text-classification", model="tabularisai/multilingual-sentiment-analysis")

def analyze_sentiment(text: str) -> dict:
    result = pipe(text)
    print("text: ", text)
    print("result: ", result)
    return result
