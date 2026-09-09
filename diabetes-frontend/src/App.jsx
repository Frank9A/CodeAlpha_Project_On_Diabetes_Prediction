import { useState } from 'react'

function App() {
  // This holds all the patient data in one place
  const [patientData, setPatientData] = useState({
    Pregnancies: 0,
    Glucose: 0,
    BloodPressure: 0,
    SkinThickness: 0,
    Insulin: 0,
    BMI: 0.0,
    DiabetesPedigreeFunction: 0.0,
    Age: 0
  })

  // This will store the final prediction sentence sent from Python
  const [predictionResult, setPredictionResult] = useState(null)

  // This updates the data whenever the doctor types in a box
  const handleChange = (e) => {
    setPatientData({
      ...patientData,
      [e.target.name]: e.target.value
    })
  }

  // This triggers when the doctor clicks "Predict"
  const handleSubmit = async (e) => {
    e.preventDefault()
    
    try {
      // 1. Send the package of data to Python
      const response = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(patientData)
      });

      // 2. Open the package Python sends back
      const data = await response.json();

      // 3. Save the final prediction sentence into our memory bank
      setPredictionResult(data.prediction);

    } catch (error) {
      console.error("Error making prediction:", error);
      setPredictionResult("Error connecting to the server.");
    }
  }

  return (
    <div style={{ padding: '20px', maxWidth: '400px', margin: 'auto' }}>
      <h2>Diabetes Prediction System</h2>
      
      <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>

        <label>Pregnancies Count:</label>
        <input type="number" name="Pregnancies" onChange={handleChange} required /> 

        <label>Glucose Level:</label>
        <input type="number" name="Glucose" onChange={handleChange} required />

        <label>Blood Pressure:</label>
        <input type="number" name="BloodPressure" onChange={handleChange} required />

        <label>Skin Thickness:</label>
        <input type="number" name="SkinThickness" onChange={handleChange} required />

        <label>Insulin Level:</label>
        <input type="number" name="Insulin" onChange={handleChange} required />

        <label>BMI:</label>
        <input type="number" step="0.1" name="BMI" onChange={handleChange} required />
        
        <label>Diabetes Pedigree Function:</label>
        <input type="number" step="0.001" name="DiabetesPedigreeFunction" onChange={handleChange} required />

        <label>Age:</label>
        <input type="number" name="Age" onChange={handleChange} required />
        
        {/* We can add the other fields (Pregnancies, Insulin, etc.) similarly! */}

        <button type="submit" style={{ marginTop: '15px', padding: '10px', cursor: 'pointer' }}>
          Predict Outcome
        </button>
      </form>
      {/* This displays the result ONLY if a prediction has been made */}
      {predictionResult && (
        <div style={{ 
          marginTop: '20px', 
          padding: '15px', 
          backgroundColor: predictionResult.includes("Positive") ? '#a7031356' : '#05ff0d26', 
          borderRadius: '5px',
          textAlign: 'center' 
        }}>
          <h3>Result: {predictionResult}</h3>
        </div>
      )}
    </div>
  )
}

export default App