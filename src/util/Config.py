from ABSA_model.ABSAModelV1 import ABSAModelV1
from util.Cors import Cors


class Config:
  def __init__(self, debug:bool, cors:Cors, model: ABSAModelV1):
    self.debug = debug
    self.cors = cors
    self.model = model