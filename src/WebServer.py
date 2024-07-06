# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# import logging
# from models.AnalyseSentimentRequest import AnalyseSentimentRequest
# from ABSA_model.ABSAModelV1 import ABSAModelV1

# # Initialize the logger...
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# # Load the model...
# model = ABSAModelV1().load_model()

# app = FastAPI(debug=True)

# origins = [
#     "http://localhost:8080",
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# @app.post("/analyse-sentiment")
# async def analyse_sentiment(payload: AnalyseSentimentRequest):
#   print(payload)
#   preds = model.predict(payload.text.split("."))
#   return {"message": preds}