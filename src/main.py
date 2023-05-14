from fastapi.responses import HTMLResponse

from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request, Form

import sentiment_analysis as se

app = FastAPI()

templates = Jinja2Templates(directory="templates/")


@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/", response_class=HTMLResponse)
async def root(request: Request, text: str = Form(''),  tool: str = Form('')):
    if tool == "textblob":
        sentiment_scores = se.get_textblob_sentiment_scores(text)
    elif tool == "vader":   
        sentiment_scores = se.get_vader_sentiment_scores(text)
    return templates.TemplateResponse("index.html", {"request": request, "sentences": sentiment_scores})
