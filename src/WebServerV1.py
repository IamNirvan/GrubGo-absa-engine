from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
from models.AnalyseSentimentRequest import AnalyseSentimentRequest
from ABSA_model.ABSAModelV1 import ABSAModelV1
from util.Config import Config
from util.Cors import Cors

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

@app.post("/analyse/sentiment")
async def analyse_sentiment(payload: AnalyseSentimentRequest):
    logging.debug("received request to analyse sentiment")
    preds = model.predict(payload.text.split("."))
    return {"message": preds}

    

