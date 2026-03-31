import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

data = pd.DataFrame({
    "typing_speed": [20, 30, 80, 90, 50, 40],
    "time_on_task": [300, 250, 60, 50, 150, 200],
    "error_count": [5, 4, 0, 1, 2, 3],
    "inactivity": [40, 35, 2, 3, 10, 20],
    "label": ["Overload", "Overload", "Underload", "Underload", "Optimal", "Optimal"]
})

X = data.drop("label", axis=1)
y = data["label"]

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, "cognitive_model.pkl")
print("Model trained successfully")
