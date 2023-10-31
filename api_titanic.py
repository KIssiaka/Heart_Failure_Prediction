import joblib
import uvicorn
from fastapi import FastAPI
import pandas as pd
from prometheus_client import Counter, make_asgi_app

survived_counter = Counter("survived", "Counter for survived")
not_survived_counter = Counter("not_survived", "Counter for not survived")

app = FastAPI()
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)


@app.get("/health_failure")
def prediction_api(age: int,anaemia: float,creatinine_phosphokinase: int,diabetes,ejection_fraction : int,high_blood_pressure : float,platelets,serum_creatinine : float,serum_sodium : float,sex : int,smoking : float,time : float,DEATH_EVENT : float
):
    model = joblib.load("mon_model.joblib")
    x = [age,anaemia,creatinine_phosphokinase,diabetes,ejection_fraction,high_blood_pressure,platelets,serum_creatinine,serum_sodium,sex,smoking,time,DEATH_EVENT
]
    prediction = model.predict(pd.DataFrame(x).transpose())
    survived = int(prediction) == 1
    if survived:
        survived_counter.inc()
    else:
        not_survived_counter.inc()
    return survived


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
