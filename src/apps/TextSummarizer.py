from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")


def summarize_text(article_text):
    result = summarizer(article_text, max_length=130, min_length=30, do_sample=False)
    print(result)
    return result

# >>> [{'summary_text': 'Liana Barrientos, 39, is charged with two counts of "offering a false instrument for filing in the first degree" In total, she has been married 10 times, with nine of her marriages occurring between 1999 and 2002. She is believed to still be married to four men.'}]

