from pydantic import BaseModel

class AnalyseSentimentRequest(BaseModel):
  text: str