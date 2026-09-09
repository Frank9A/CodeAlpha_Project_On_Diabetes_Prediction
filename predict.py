import joblib
import pandas as pd

#1. Load th e saved model
loaded_model = joblib.load('diabetes_model.pkl')

#2. Create data for a brand new, imaginary patient
# These columns must match the exact order and name  of the original dataset
new_patient_data = pd.DataFrame([{
    'Pregnancies': 2,
    'Glucose': 145,
    'BloodPressure': 82,
    'SkinThickness': 25,
    'Insulin': 120,
    'BMI': 29.5,
    'DiabetesPedigreeFunction': 0.45,
    'Age': 41
}])

#3. Ask the loaded model to predict the outcome
prediction = loaded_model.predict(new_patient_data)

#4. Display a clean, readable result
print("\n--- New Patient Prediction ---")
if prediction[0] == 1:
    print("Result: High risk of diabetes (Positive)")
else:
    print("Result: Low risk of diabetes (Negative)")