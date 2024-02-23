Diabetes Prediction API
* This repository contains the code for a web API that can be used to predict the risk of diabetes. The API is built using FastAPI and uses a machine learning model that has been trained on data from real patients.

How to use the API: 
* Clone this repository to your local machine.
* Make sure you have the following Python libraries installed:
1. fastapi
2. uvicorn
3. pydantic
4. json
5. pickle
6. scikit-learn
7. requests
* Run the uvicorn ml_api:app --host 0.0.0.0 --port 8000 command.
* Send a POST request to the http://localhost:8000/diabetes_predicton endpoint with the following JSON data in the body:

JSON
{
  "Pregnancies": 6,
  "Glucose": 148,
  "BloodPressure": 72,
  "SkinThickness": 35,
  "Insulin": 0,
  "BMI": 33.6,
  "DiabetesPedigreeFunction": 0.627,
  "Age": 50
}

* The API will respond with a JSON object that contains the predicted risk of diabetes.

* Example Usage: 
Bash
curl -X POST http://localhost:8000/diabetes_predicton -H 'Content-Type: application/json' -d '{"Pregnancies": 6, "Glucose": 148, "BloodPressure": 72, "SkinThickness": 35, "Insulin": 0, "BMI": 33.6, "DiabetesPedigreeFunction": 0.627, "Age": 50}'
Use code with caution.
JSON
{
  "message": "the person is diabetic"
}

Disclaimer:
* This API is for informational purposes only and should not be used as a substitute for professional medical advice. If you are concerned about your risk of developing diabetes, please consult with a doctor.

How to contribute:
* We welcome contributions to this project. If you would like to contribute, please fork the repository and create a pull request.
