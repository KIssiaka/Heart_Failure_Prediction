import requests
import joblib
import uvicorn
from fastapi import FastAPI
import pandas as pd
from prometheus_client import Counter, make_asgi_app
import xgboost as xgb
from typing import Optional, List
from pydantic import BaseModel

# Charger le modèle XGBoost depuis le fichier Joblib
model = joblib.load("mon_model.joblib")


class User(BaseModel):
    age: int
    anaemia: int
    creatinine_phosphokinase: int
    diabetes: int
    ejection_fraction: int
    high_blood_pressure: int
    platelets: int
    serum_creatinine: int
    serum_sodium: int
    sex: int
    smoking: int
    time: int


user_data = {
    "age": 75,
    "anaemia": 1,
    "creatinine_phosphokinase": 2000,
    "diabetes": 1,
    "ejection_fraction": 2,
    "high_blood_pressure": 3,
    "platelets": 1,
    "serum_creatinine": 4,
    "serum_sodium": 5,
    "sex": 6,
    "smoking": 4,
    "time": 5
}

user = User(**user_data)

app = FastAPI()
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)


@app.get("/")  # It's the base of the server in the Webapp
async def get_root():
    return {"hello world"}


@app.get("/heart_failure")
async def func():
    return user


@app.post("/heart_failure")
async def prediction_api(user: User):
    try:
        # Créez un dictionnaire à partir des valeurs de l'objet user
        user_data = user.dict()

        # Créez un DataFrame à partir du dictionnaire
        user_df = pd.DataFrame([user_data])

        # Faites la prédiction avec les données de l'utilisateur
        prediction = model.predict(user_df)
        survived = int(prediction[0]) == 1

        return {"survived": survived}

    except Exception as e:
        return {"error": str(e)}


# URL de votre serveur FastAPI
# api_url = "http://127.0.0.1:8000/heart_failure"

# Données de test pour la prédiction

# Faites une requête POST pour obtenir la prédiction
# response = requests.get(api_url, params=data)

# Afficher la réponse
# print(response.json())


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
