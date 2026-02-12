from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import joblib

from agents.planner import planner_agent
from agents.executor import executor_agent
from agents.reflection import reflection_agent
from tools.genai_tool import generate_advice

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load("ml/cognitive_model.pkl")

class InputData(BaseModel):
    typing_speed: int
    time_on_task: int
    error_count: int
    inactivity: int

@app.post("/analyze")
def analyze(data: InputData):
    X = pd.DataFrame([data.dict()])
    cognitive_load = model.predict(X)[0]

    decision = planner_agent(cognitive_load)
    execution = executor_agent(decision)
    advice = generate_advice(cognitive_load)
    reflection = reflection_agent(cognitive_load)

    return {
        "cognitive_load": cognitive_load,
        "decision": decision,
        "execution": execution,
        "advice": advice,
        "reflection": reflection
    }
