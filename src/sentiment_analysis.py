from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def get_textblob_sentiment_scores(text):
    blob = TextBlob(text)
    sentences_sentiment_scores = []
    for sentence in blob.sentences:
        
        #Polarity : [-1,1] where -1 is negative and 1 is positive
        sentiment_polarity = sentence.sentiment.polarity
        #Subjectivity : [0,1] where 0 is objective and 1 is subjective
        sentiment_subjectivity = sentence.sentiment.subjectivity
        
        sentences_sentiment_scores.append(
            {'sentence': str(sentence), 'sentiment_polarity': sentiment_polarity, 'sentiment_subjectivity': sentiment_subjectivity})
        
    return sentences_sentiment_scores

def get_vader_sentiment_scores(text):
    blob = TextBlob(text)
    vaderAnalyzer = SentimentIntensityAnalyzer()
    sentences_sentiment_scores = []
    for sentence in blob.sentences:
        
        sentiment = vaderAnalyzer.polarity_scores(sentence)
        #Compound: (negative sentiment) <= -0.05 (neutral sentiment) >= 0.05( positive sentiment)
        sentiment_polarity = sentiment['compound'] if abs(sentiment['compound']) >= 0.5 else 0
        sentiment_subjectivity = 1-sentiment['neu']
        
        sentences_sentiment_scores.append(
            {'sentence': str(sentence), 'sentiment_polarity': sentiment_polarity, 'sentiment_subjectivity': sentiment_subjectivity})
        
    return sentences_sentiment_scores
