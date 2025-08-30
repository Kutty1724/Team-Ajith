from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Medical Advisor API")

# Simple symptom-to-medicine dictionary with doses
medical_data = {
    "fever": {"medicine": "Paracetamol", "dosage": "500 mg every 6-8 hours (max 4g/day)"},
    "headache": {"medicine": "Ibuprofen", "dosage": "400 mg every 6 hours as needed"},
    "cold": {"medicine": "Cetirizine", "dosage": "10 mg once daily"},
    "cough": {"medicine": "Dextromethorphan Syrup", "dosage": "10 ml every 6 hours"},
    # ... add more symptoms here
}

# Request models

class SymptomRequest(BaseModel):
    age: int
    weight: float
    text: str  # Symptoms input, comma separated

class PrescriptionRequest(BaseModel):
    text: str  # Medicine names, comma separated

# Helper functions

def get_advice_for_symptoms(text: str):
    symptoms = [s.strip().lower() for s in text.split(",")]
    advice = []
    for symptom in symptoms:
        if symptom in medical_data:
            advice.append({
                "symptom": symptom,
                "medicine": medical_data[symptom]["medicine"],
                "dosage": medical_data[symptom]["dosage"]
            })
    return advice

def check_drug_interactions(meds_list):
    # Dummy placeholder: no interactions found
    return {"message": "No interactions found for given medicines."}

def get_dosage_and_alternatives(meds_list):
    dosage_info = {}
    for med in meds_list:
        dosage_info[med] = {
            "dosage": f"Standard dosage for {med}",
            "alternatives": [
                f"Alternative 1 for {med}",
                f"Alternative 2 for {med}"
            ]
        }
    return dosage_info

# API endpoints

@app.post("/analyze")
def analyze(request: SymptomRequest):
    advice = get_advice_for_symptoms(request.text)
    if not advice:
        return {"message": "No medicine advice found for the symptoms."}
    return {
        "age": request.age,
        "weight": request.weight,
        "recommendations": advice
    }

@app.post("/check_interactions")
def check_interactions(request: PrescriptionRequest):
    meds = [m.strip() for m in request.text.split(",")]
    interactions = check_drug_interactions(meds)
    return {"medicines": meds, "interactions": interactions}

@app.post("/check_dosage_alternatives")
def check_dosage_alternatives(request: PrescriptionRequest):
    meds = [m.strip() for m in request.text.split(",")]
    dosage_info = get_dosage_and_alternatives(meds)
    return {"dosage_info": dosage_info}
# Your existing last endpoint starts around line 70-79

@app.post("/check_dosage_alternatives")
def check_dosage_alternatives(request: PrescriptionRequest):
    meds = [m.strip() for m in request.text.split(",")]
    dosage_info = get_dosage_and_alternatives(meds)
    return {"dosage_info": dosage_info}

# Add this new test endpoint at line 80:

@app.get("/test")
def health_check():
    return {"hello": "world"}
