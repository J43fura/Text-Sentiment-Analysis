from textblob import TextBlob
import nltk


def get_sentiment_scores(text):
    blob = TextBlob(text)
    paragraph_sentiment_scores = []
    for sentence in blob.sentences:
        sentiment_polarity = sentence.sentiment.polarity
        sentiment_subjectivity = sentence.sentiment.subjectivity
        paragraph_sentiment_scores.append(
            {'sentence': str(sentence), 'sentiment_polarity': sentiment_polarity, 'sentiment_subjectivity': sentiment_subjectivity})
    return paragraph_sentiment_scores
