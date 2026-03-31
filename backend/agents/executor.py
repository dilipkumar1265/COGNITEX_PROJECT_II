# backend/agents/executor.py

def executor_agent(decision):
    mapping = {
        "Increase difficulty": "Loading harder content",
        "Maintain pace": "Continuing current flow",
        "Reduce difficulty": "Simplifying tasks and suggesting break"
    }
    return mapping[decision]
