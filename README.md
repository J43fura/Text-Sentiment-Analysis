# Text Sentiment Analysis

#### Color-Coded Text Sentiment Analysis (also known as opinion mining or emotion AI) using [TextBlob](https://textblob.readthedocs.io/en/dev/) / [VADER](https://github.com/cjhutto/vaderSentiment) for NLP.

![image](https://github.com/J43fura/Text-Sentiment-Analysis/assets/73950268/71348abf-d892-41dc-80ab-633cc7289dcf)
_Objective & Positive, Objective & Negative, Subjective & Positive, Subjective & Negative and Neutral._

**Setup:**

- `pip install -r requirements.txt`
- `python -m textblob.download_corpora`

Execute in src:

- `py -m uvicorn main:app --reload`

This app uses [FastAPI](https://fastapi.tiangolo.com/lo/), [TextBlob](https://textblob.readthedocs.io/en/dev/), [VADER](https://github.com/cjhutto/vaderSentiment), [simplecss](https://simplecss.org/).
