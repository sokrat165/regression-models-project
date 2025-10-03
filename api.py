import numpy as np
import json
import logging
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
scaler = joblib.load("scaler.joblib")
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_methods=["*"],
    allow_headers=["*"],
)
with open("linear_params.json") as f:
    params = json.load(f)
class PlayerInput(BaseModel):
    AtBat: float
    Hits: float
    HmRun: float
    Runs: float
    RBI: float
    Walks: float
    Years: float
    CAtBat: float
    CHits: float
    CHmRun: float
    CRuns: float
    CRBI: float
    CWalks: float
    PutOuts: float
    Assists: float
    Errors: float
    League: str
    Division: str
    NewLeague: str
def preprocess(data: PlayerInput):
    if data.League not in ['A', 'N']:
        raise HTTPException(status_code=400, detail="League must be 'A' or 'N'")
    if data.Division not in ['E', 'W']:
        raise HTTPException(status_code=400, detail="Division must be 'E' or 'W'")
    if data.NewLeague not in ['A', 'N']:
        raise HTTPException(status_code=400, detail="NewLeague must be 'A' or 'N'")
    
    league_N = 1 if data.League == "N" else 0
    division_W = 1 if data.Division == "W" else 0
    newleague_N = 1 if data.NewLeague == "N" else 0
    
    features = [
        data.AtBat, data.Hits, data.HmRun, data.Runs, data.RBI, data.Walks, data.Years,
        data.CAtBat, data.CHits, data.CHmRun, data.CRuns, data.CRBI, data.CWalks,
        data.PutOuts, data.Assists, data.Errors,
        league_N, division_W, newleague_N
    ]
    for i, field in enumerate(['AtBat', 'Hits', 'HmRun', 'Runs', 'RBI', 'Walks', 'Years', 
                              'CAtBat', 'CHits', 'CHmRun', 'CRuns', 'CRBI', 'CWalks', 
                              'PutOuts', 'Assists', 'Errors']):
        if features[i] < 0:
            raise HTTPException(status_code=400, detail=f"{field} cannot be negative")
    return np.array(features)
@app.post("/predict")
def predict_salary(player: PlayerInput):
    logger.info(f"Received input: {player.dict()}")
    coef = np.array(params["ridge_coef"])
    intercept = params["ridge_intercept"]
    features = preprocess(player)
    features_scaled = scaler.transform([features])[0]
    if len(coef) != len(features_scaled):
        raise HTTPException(status_code=500, detail="Model coefficients do not match feature count")
    salary = float(np.dot(features_scaled, coef) + intercept)
    logger.info(f"Predicted salary: {salary}")
    return {"salary": salary}