# Sentiment-analysis-engine

This system is responsible for performing **Aspect Based Sentiment Analysis (ABSA)** on reviews. This is part of
my final year project in my BEng (Hons) Topup programme.

## Running the application
- Activate the python environment 
```powershell
.\env\Scripts\activate
```
- Navigate into the `\src` directory
- Execute following command
```powershell
uvicorn WebServerV1:app --reload
```