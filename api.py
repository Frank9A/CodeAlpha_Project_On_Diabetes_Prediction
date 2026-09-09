from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import joblib
import pydantic
from pydantic import BaseModel
import pandas as pd


#initialize the server
app = FastAPI()

#Allow React to commmunicate with this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Load your trained machine learning model into the memory
model = joblib.load('diabetes_model.pkl')

#Define the extact structure of the data React will send
class PatientData(BaseModel):
    Pregnancies: int
    Glucose: float
    BloodPressure: float
    SkinThickness: float
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int

#5. Create the Prediction endpiont
@app.post("/predict")
def make_prediction(data: PatientData):
    #Convert the incoming data into a Pandas Dataframe
    input_data = pd.DataFrame([data.dict()])

    #Hand the data to the model for prediction 
    prediction = model.predict(input_data)

    #Translate the 0 oer 1 into plane English
    result = "High risk of diabetes (Positive)" if prediction[0] == 1 else "Low risk of diabetes (Negative)"

    #Send the result back to React
    return {"prediction": result}