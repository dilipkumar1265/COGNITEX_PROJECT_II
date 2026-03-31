# backend/agents/reflection.py

def reflection_agent(cognitive_load):
    if cognitive_load == "Underload":
        return "Learner engagement is low, increasing challenge"
    elif cognitive_load == "Optimal":
        return "Stable learning state maintained"
    else:
        return "High cognitive load detected, intervention applied"
