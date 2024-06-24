from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
from models.AnalyseSentimentRequest import AnalyseSentimentRequest

# Initialize the logger...
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

app = FastAPI(debug=True)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
  return {"message": "Yeah buddy!"}

@app.post("/analyse-sentiment")
async def analyse_sentiment(payload: AnalyseSentimentRequest):
  print(payload)
  logging.debug("extract the request")
  logging.debug("extract the review to be analysed...")
  logging.debug("load the model...")
  logging.debug("analyse the sentiment...")
  return {"message": "Analyse sentiment endpoint"}