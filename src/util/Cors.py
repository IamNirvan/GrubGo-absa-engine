class Cors:
   def __init__(self, allow_origins:list, allow_credentials:bool, allow_methods:list, allow_headers:list):
      self.allow_origins = allow_origins
      self.allow_credentials = allow_credentials
      self.allow_methods = allow_methods
      self.allow_headers = allow_headers