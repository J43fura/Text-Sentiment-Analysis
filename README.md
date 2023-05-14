# Text Sentiment Analysis

#### Color-Coded Text Sentiment Analysis (also known as opinion mining or emotion AI) using [TextBlob](https://textblob.readthedocs.io/en/dev/) for NLP.

![image](https://github.com/J43fura/Text-Sentiment-Analysis/assets/73950268/71348abf-d892-41dc-80ab-633cc7289dcf)
_Objective & Positive, Objective & Negative, Subjective & Positive, Subjective & Negative and Neutral._

**Installations:**

NLP

- `py -m pip install -U textblob`
- `py -m textblob.download_corpora`
- `py -m pip install vadersentiment`

FastAPI

- `py -m pip install "fastapi[all]"`
- `py -m pip install "uvicorn[standard]"`

Execute

- `py -m uvicorn main:app --reload`

This app uses [FastAPI](https://fastapi.tiangolo.com/lo/), [TextBlob](https://textblob.readthedocs.io/en/dev/), [simplecss](https://simplecss.org/).
