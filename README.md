# Text Sentiment Analysis
This is a Color-Coded Text Sentiment Analysis

![image](https://github.com/J43fura/Text-Sentiment-Analysis/assets/73950268/942d6d75-6639-448b-bece-0873a64a10f3)
_Objective & Positive, Objective & Negative, Subjective & Positive, Subjective & Negative and Neutral._

**Current Models/Tools:**
-  [TextBlob](https://textblob.readthedocs.io/en/dev/) 
-  [VADER](https://github.com/cjhutto/vaderSentiment) 

Setup
--
- `pip install -r requirements.txt`
- `python -m textblob.download_corpora`

Execution
--
- `cd src`
- `python -m uvicorn main:app --reload`

This app uses 
--
- Models
  - [TextBlob](https://textblob.readthedocs.io/en/dev/)
  - [VADER](https://github.com/cjhutto/vaderSentiment)
- Python Framework
  - [FastAPI](https://fastapi.tiangolo.com/lo/)
    - Template engine:
      - [Jinja2](https://fastapi.tiangolo.com/advanced/templates/)   
- Styling
  - [simplecss](https://simplecss.org/)
