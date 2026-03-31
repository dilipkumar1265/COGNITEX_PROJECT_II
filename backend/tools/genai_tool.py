# backend/tools/genai_tool.py

def generate_advice(cognitive_load):
    advice_map = {
        "Underload": "Try more challenging tasks to stay engaged.",
        "Optimal": "Continue at the current pace for effective learning.",
        "Overload": "Take a short break and resume with simpler tasks."
    }
    return advice_map[cognitive_load]
