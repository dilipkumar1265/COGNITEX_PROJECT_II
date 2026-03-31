# backend/agents/planner.py

def planner_agent(cognitive_load):
    if cognitive_load == "Underload":
        return "Increase difficulty"
    elif cognitive_load == "Optimal":
        return "Maintain pace"
    else:
        return "Reduce difficulty"
