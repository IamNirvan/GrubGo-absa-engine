from pydantic import BaseModel
from typing import List

class AnalyseSentimentRequestV2(BaseModel):
    text: List[str]