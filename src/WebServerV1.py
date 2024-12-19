from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
from DTO.AnalyseSentimentRequest import AnalyseSentimentRequest
from DTO.AnalyseSentimentRequestV2 import AnalyseSentimentRequestV2
from ABSA_model.ABSAModelV1 import ABSAModelV1
from util.Config import Config
from util.Cors import Cors
import re

class WebServerV1 :
    def __init__(self, config:Config):
       self.config = config
       self.app:FastAPI = self.init_server()

    def init_server(self) -> FastAPI:
       app = FastAPI(debug=self.config.debug)
       app.add_middleware(
            CORSMiddleware,
            allow_origins=self.config.cors.allow_origins,
            allow_credentials=self.config.cors.allow_credentials,
            allow_methods=self.config.cors.allow_methods,
            allow_headers=self.config.cors.allow_headers,
        )
       return app

# Initialize the logger...
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Configure cors
corsConfig = Cors(
    allow_origins=["http://localhost:8080",],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the fine-tuned model
model = ABSAModelV1().load_model()
logging.debug("Model loaded successfully")

# Assemble the config object
config = Config(
    debug=True, 
    cors=corsConfig,
    model=model
)
logging.debug("Config object created successfully")

# Create instance of the web server
app = WebServerV1(
    config=config
).app
logging.debug("Web server created successfully")

@app.post("/v1/analyse/sentiment")
async def analyse_sentiment(payload: AnalyseSentimentRequest):
    logging.debug("received request to analyse sentiment")
    preds = model.predict(payload.text.split("."))
    
    # Flatten the nested lists
    flattened_preds = [item for sublist in preds for item in sublist]
    
    return flattened_preds
    
@app.post("/v2/analyse/sentiment")
async def analyse_sentiment_v2(payload: AnalyseSentimentRequestV2):
    logging.debug("received request to analyse sentiment v2")

    sentences = []
    for text in payload.text:
        sentences.extend(re.split(r'[.!?]', text))
    
    preds = model.predict(sentences)
    flattened_preds = [item for sublist in preds for item in sublist]

    # Group spans by their text and count polarities
    span_dict = {}
    for pred in flattened_preds:
        span = pred['span']
        polarity = pred['polarity']
        if span not in span_dict:
            span_dict[span] = {'positive': 0, 'neutral': 0, 'negative': 0}
        span_dict[span][polarity] += 1

    # Calculate the ratio of polarities for each span as percentages
    grouped_preds = []
    for span, counts in span_dict.items():
        total = counts['positive'] + counts['neutral'] + counts['negative']
        ratio = {
            'span': span,
            'positiveRatio': round((counts['positive'] / total * 100), 2) if total > 0 else 0,
            'neutralRatio': round((counts['neutral'] / total * 100), 2) if total > 0 else 0,
            'negativeRatio': round((counts['negative'] / total * 100), 2) if total > 0 else 0
        }
        grouped_preds.append(ratio)

    return grouped_preds

    

