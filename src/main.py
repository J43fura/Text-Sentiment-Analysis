from fastapi.responses import HTMLResponse

from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request, Form

from fastapi.staticfiles import StaticFiles
from pathlib import Path

import sentiment_analysis as se

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.absolute() / "static"),
    name="static",
)

templates = Jinja2Templates(directory="templates/")


@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/", response_class=HTMLResponse)
async def root(request: Request, text: str = Form(...)):
    sentiment_scores = se.get_sentiment_scores(text)
    return templates.TemplateResponse("index.html", {"request": request, "sentences": sentiment_scores})
