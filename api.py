import joblib
import uvicorn
from fastapi import FastAPI
import pandas as pd
from prometheus_client import make_asgi_app
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


app = FastAPI()
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)


@app.get("/")  # It's the base of the server in the Webapp
async def get_root():
    return {"hello world"}


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

        return {"Le résultat de la survie du patient est ": survived}

    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
