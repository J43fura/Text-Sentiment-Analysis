# Text Sentiment Analysis

#### Text Color-Coded Sentiment Analysis (also known as opinion mining or emotion AI)

**Installations:**

NLP

- `py -m pip install -U textblob`
- `py -m textblob.download_corpora`

FastAPI

- `py -m pip install fastapi`
- `py -m pip install "uvicorn[standard]"`

- `py -m uvicorn main:app --reload`

**Imports:**

NLP

- `from textblob import TextBlob`
- `import nltk`

FastAPI

- `from fastapi.responses import HTMLResponse`
- `from fastapi.templating import Jinja2Templates`
- `from fastapi import FastAPI, Request, Form`

- `import sentiment_analysis as se`
