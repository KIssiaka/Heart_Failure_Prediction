"""async def prediction_api(age: int, anaemia: int, creatinine_phosphokinase: int, diabetes: int, ejection_fraction: int,
                         high_blood_pressure: int, platelets: int, serum_creatinine: int,
                         serum_sodium: int, sex: int, smoking: int, time: int):
    
    try:
        x = [age, anaemia, creatinine_phosphokinase, diabetes,
             ejection_fraction, high_blood_pressure, platelets,
             serum_creatinine, serum_sodium, sex, smoking, time]
        prediction = model.predict(pd.DataFrame(x).transpose())
        survived = int(prediction[0]) == 1

        return {"survived": survived}

    except Exception as e:
        return {"error": str(e)}"""
