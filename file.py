"""
🔬 Disease Prediction & Risk Classification Engine
Rule-based system with city trend integration
"""

import re
from data import CITY_DISEASE_DATA, VOICE_PATTERNS


def predict_disease(symptoms: list, city: str, age: int) -> dict:
    """
    Predict diseases based on symptoms, city trends, and age.
    
    Args:
        symptoms: List of symptom strings
        city: Patient's city
        age: Patient's age
        
    Returns:
        Dictionary of {disease_name: probability_percentage}
    """
    predictions = {}
    symptoms_lower = [s.lower() for s in symptoms]
    city_data = CITY_DISEASE_DATA.get(city, {}).get("diseases", {})
    
    # ========== DENGUE DETECTION ==========
    dengue_symptoms = ["fever", "rash", "headache", "body pain", "joint pain", "fatigue"]
    dengue_match = sum(1 for s in symptoms_lower if s in dengue_symptoms)
    if dengue_match >= 2:
        base_prob = 35 + (dengue_match * 12)
        # City outbreak bonus
        if city_data.get("Dengue", {}).get("risk") == "HIGH":
            base_prob += 20
        elif city_data.get("Dengue", {}).get("risk") == "MEDIUM":
            base_prob += 10
        # Characteristic combination
        if "fever" in symptoms_lower and "rash" in symptoms_lower:
            base_prob += 15
        predictions["Dengue"] = min(base_prob, 95)
    
    # ========== TB DETECTION ==========
    tb_symptoms = ["cough", "night sweats", "weight loss", "fever", "fatigue", "loss of appetite", "chest pain"]
    tb_match = sum(1 for s in symptoms_lower if s in tb_symptoms)
    if tb_match >= 2:
        base_prob = 25 + (tb_match * 10)
        # Chronic cough indicator
        if "cough" in symptoms_lower:
            base_prob += 15
            if tb_match >= 3:
                base_prob += 10
        # Age factor
        if age > 50:
            base_prob += 8
        predictions["Tuberculosis (TB)"] = min(base_prob, 90)
    
    # ========== MALARIA DETECTION ==========
    malaria_symptoms = ["fever", "cold", "headache", "nausea", "vomiting", "fatigue", "body pain"]
    malaria_match = sum(1 for s in symptoms_lower if s in malaria_symptoms)
    if malaria_match >= 2 and "fever" in symptoms_lower:
        base_prob = 30 + (malaria_match * 10)
        # Cyclic fever pattern
        if "cold" in symptoms_lower and "fever" in symptoms_lower:
            base_prob += 15
        # City outbreak
        if city_data.get("Malaria", {}).get("risk") == "HIGH":
            base_prob += 15
        predictions["Malaria"] = min(base_prob, 88)
    
    # ========== TYPHOID DETECTION ==========
    typhoid_symptoms = ["fever", "abdominal pain", "headache", "loss of appetite", "diarrhea", "fatigue"]
    typhoid_match = sum(1 for s in symptoms_lower if s in typhoid_symptoms)
    if typhoid_match >= 2:
        base_prob = 28 + (typhoid_match * 11)
        # Characteristic pattern
        if "fever" in symptoms_lower and "abdominal pain" in symptoms_lower:
            base_prob += 15
        # City factor
        if city_data.get("Typhoid", {}).get("risk") == "HIGH":
            base_prob += 18
        predictions["Typhoid"] = min(base_prob, 85)
    
    # ========== VIRAL FLU DETECTION ==========
    flu_symptoms = ["fever", "cough", "cold", "headache", "body pain", "fatigue", "nausea"]
    flu_match = sum(1 for s in symptoms_lower if s in flu_symptoms)
    if flu_match >= 2:
        base_prob = 40 + (flu_match * 8)
        # Common combination
        if "fever" in symptoms_lower and "cough" in symptoms_lower:
            base_prob += 10
        predictions["Viral Flu"] = min(base_prob, 92)
    
    # ========== RESPIRATORY INFECTION ==========
    resp_symptoms = ["cough", "breathlessness", "chest pain", "fever", "cold", "fatigue"]
    resp_match = sum(1 for s in symptoms_lower if s in resp_symptoms)
    if resp_match >= 2:
        base_prob = 30 + (resp_match * 12)
        # Severity indicators
        if "breathlessness" in symptoms_lower:
            base_prob += 15
        if "chest pain" in symptoms_lower:
            base_prob += 12
        # Age vulnerability
        if age > 60:
            base_prob += 15
        elif age < 5:
            base_prob += 10
        predictions["Respiratory Infection"] = min(base_prob, 90)
    
    # ========== GASTROENTERITIS ==========
    gastro_symptoms = ["nausea", "vomiting", "diarrhea", "abdominal pain", "fever", "loss of appetite"]
    gastro_match = sum(1 for s in symptoms_lower if s in gastro_symptoms)
    if gastro_match >= 2:
        base_prob = 35 + (gastro_match * 10)
        # GI specific
        if "vomiting" in symptoms_lower and "diarrhea" in symptoms_lower:
            base_prob += 15
        predictions["Gastroenteritis"] = min(base_prob, 88)
    
    # Sort by probability (highest first)
    predictions = dict(sorted(predictions.items(), key=lambda x: x[1], reverse=True))
    
    return predictions


def calculate_risk_score(
    symptoms: list,
    age: int,
    bp_systolic: int,
    bp_diastolic: int,
    pulse: int,
    city: str,
    predictions: dict
) -> dict:
    """
    Calculate comprehensive risk score and category.
    
    Args:
        symptoms: List of symptoms
        age: Patient age
        bp_systolic: Systolic blood pressure
        bp_diastolic: Diastolic blood pressure
        pulse: Heart rate
        city: Patient city
        predictions: Disease predictions dict
        
    Returns:
        Dictionary with score, category, and risk factors
    """
    risk_score = 0
    risk_factors = []
    
    # ========== AGE FACTOR ==========
    if age >= 75:
        risk_score += 35
        risk_factors.append("Very Elderly (75+)")
    elif age >= 65:
        risk_score += 25
        risk_factors.append("Elderly (65+)")
    elif age >= 55:
        risk_score += 15
        risk_factors.append("Senior (55+)")
    elif age <= 2:
        risk_score += 30
        risk_factors.append("Infant (0-2 years)")
    elif age <= 5:
        risk_score += 20
        risk_factors.append("Young Child (2-5 years)")
    
    # ========== SYMPTOM COUNT ==========
    symptom_count = len(symptoms)
    if symptom_count >= 6:
        risk_score += 30
        risk_factors.append(f"Many symptoms ({symptom_count})")
    elif symptom_count >= 4:
        risk_score += 20
        risk_factors.append(f"Multiple symptoms ({symptom_count})")
    elif symptom_count >= 2:
        risk_score += 10
    
    # ========== CRITICAL SYMPTOMS ==========
    critical_symptoms = {
        "breathlessness": 25,
        "chest pain": 25,
        "jaundice": 20,
        "vomiting": 10,
        "diarrhea": 10
    }
    symptoms_lower = [s.lower() for s in symptoms]
    
    for symptom, score in critical_symptoms.items():
        if symptom in symptoms_lower:
            risk_score += score
            if score >= 20:
                risk_factors.append(f"Critical: {symptom.title()}")
    
    # ========== VITAL SIGNS ==========
    if bp_systolic > 0 and bp_diastolic > 0:
        # Hypertensive crisis
        if bp_systolic >= 180 or bp_diastolic >= 120:
            risk_score += 35
            risk_factors.append("⚠️ Hypertensive Crisis")
        # Stage 2 hypertension
        elif bp_systolic >= 140 or bp_diastolic >= 90:
            risk_score += 18
            risk_factors.append("High Blood Pressure")
        # Hypotension
        elif bp_systolic < 90 or bp_diastolic < 60:
            risk_score += 22
            risk_factors.append("Low Blood Pressure")
    
    if pulse > 0:
        if pulse > 120:
            risk_score += 18
            risk_factors.append("Tachycardia (Rapid Heart)")
        elif pulse > 100:
            risk_score += 10
            risk_factors.append("Elevated Heart Rate")
        elif pulse < 50:
            risk_score += 18
            risk_factors.append("Bradycardia (Slow Heart)")
    
    # ========== CITY OUTBREAK FACTOR ==========
    city_data = CITY_DISEASE_DATA.get(city, {}).get("diseases", {})
    high_risk_count = sum(1 for d in city_data.values() if d.get("risk") == "HIGH")
    
    if high_risk_count >= 4:
        risk_score += 20
        risk_factors.append(f"City outbreak zone ({high_risk_count} diseases)")
    elif high_risk_count >= 2:
        risk_score += 12
        risk_factors.append(f"City has active outbreaks")
    elif high_risk_count >= 1:
        risk_score += 6
    
    # ========== DISEASE PREDICTION SEVERITY ==========
    if predictions:
        top_prob = list(predictions.values())[0]
        top_disease = list(predictions.keys())[0]
        
        if top_prob >= 85:
            risk_score += 25
            risk_factors.append(f"High probability: {top_disease}")
        elif top_prob >= 70:
            risk_score += 15
            risk_factors.append(f"Likely: {top_disease}")
        elif top_prob >= 55:
            risk_score += 8
    
    # ========== CALCULATE FINAL CATEGORY ==========
    risk_score = min(risk_score, 100)
    
    if risk_score >= 70:
        category = "HIGH"
    elif risk_score >= 40:
        category = "MEDIUM"
    else:
        category = "LOW"
    
    return {
        "score": risk_score,
        "category": category,
        "factors": risk_factors
    }


def parse_voice_input(text: str, language: str = "English") -> dict:
    """
    Parse voice input to extract patient data.
    
    Args:
        text: Raw voice transcript
        language: Selected language
        
    Returns:
        Dictionary with extracted fields
    """
    result = {
        "name": "",
        "age": 0,
        "symptoms": [],
        "bp": "",
        "gender": "",
        "bulk_mode": False,
        "patient_range": None
    }
    
    text_lower = text.lower()
    
    # ========== BULK MODE DETECTION ==========
    bulk_patterns = [
        r"patients?\s+(\d+)\s*(?:to|-)\s*(\d+)",
        r"(\d+)\s*(?:to|-)\s*(\d+)\s*patients?"
    ]
    for pattern in bulk_patterns:
        bulk_match = re.search(pattern, text_lower)
        if bulk_match:
            result["bulk_mode"] = True
            result["patient_range"] = (int(bulk_match.group(1)), int(bulk_match.group(2)))
            break
    
    # ========== NAME EXTRACTION ==========
    name_patterns = [
        r"(?:patient|name|naam|નામ|मरीज)\s+([a-zA-Z\u0900-\u097F\u0A80-\u0AFF]+)",
        r"^([A-Z][a-z]+)\s+(?:age|has|is)"
    ]
    for pattern in name_patterns:
        name_match = re.search(pattern, text, re.IGNORECASE)
        if name_match:
            result["name"] = name_match.group(1).strip().title()
            break
    
    # ========== AGE EXTRACTION ==========
    age_patterns = [
        r"age\s+(\d+)",
        r"(\d+)\s*(?:years?|yrs?|साल|વર્ષ)\s*old",
        r"उम्र\s+(\d+)",
        r"ઉંમર\s+(\d+)"
    ]
    for pattern in age_patterns:
        age_match = re.search(pattern, text_lower)
        if age_match:
            result["age"] = int(age_match.group(1))
            break
    
    # ========== GENDER EXTRACTION ==========
    if any(g in text_lower for g in ["male", "man", "पुरुष", "પુરુષ"]):
        result["gender"] = "M"
    elif any(g in text_lower for g in ["female", "woman", "महिला", "સ્ત્રી"]):
        result["gender"] = "F"
    
    # ========== BP EXTRACTION ==========
    bp_patterns = [
        r"bp\s+(\d+)[/\s]+(\d+)",
        r"blood\s+pressure\s+(\d+)[/\s]+(\d+)",
        r"(\d{2,3})[/](\d{2,3})"
    ]
    for pattern in bp_patterns:
        bp_match = re.search(pattern, text_lower)
        if bp_match:
            result["bp"] = f"{bp_match.group(1)}/{bp_match.group(2)}"
            break
    
    if "bp normal" in text_lower or "normal bp" in text_lower:
        result["bp"] = "120/80"
    
    # ========== SYMPTOM EXTRACTION ==========
    # Get language-specific patterns
    lang_key = "english"
    if "हिंदी" in language or "hindi" in language.lower():
        lang_key = "hindi"
    elif "ગુજરાતી" in language or "gujarati" in language.lower():
        lang_key = "gujarati"
    
    # Check all languages for symptoms
    for lang, patterns in VOICE_PATTERNS.items():
        for keyword, symptom in patterns.get("symptoms", {}).items():
            if keyword in text.lower() or keyword in text:
                if symptom not in result["symptoms"]:
                    result["symptoms"].append(symptom)
    
    return result


def generate_patient_summary(patient_data: dict, predictions: dict, risk: dict) -> str:
    """
    Generate formatted summary for WhatsApp/SMS.
    
    Args:
        patient_data: Patient information dictionary
        predictions: Disease predictions
        risk: Risk assessment results
        
    Returns:
        Formatted string summary
    """
    # Get top prediction
    top_disease = "Assessment Needed"
    top_prob = 0
    if predictions:
        top_disease = list(predictions.keys())[0]
        top_prob = list(predictions.values())[0]
    
    # Risk emoji
    risk_emoji = "🔴" if risk['category'] == "HIGH" else "🟡" if risk['category'] == "MEDIUM" else "🟢"
    
    # Format symptoms
    symptoms_str = ", ".join(patient_data.get('symptoms', [])) or "Not recorded"
    
    # Format risk factors
    factors_str = "\n".join(f"  • {f}" for f in risk.get('factors', [])[:5]) or "  • None identified"
    
    summary = f"""🏥 *PATIENT ALERT - {risk['category']} RISK* {risk_emoji}

👤 *Patient:* {patient_data.get('name', 'N/A')}
📅 *Age/Gender:* {patient_data.get('age', 'N/A')} / {patient_data.get('gender', 'N/A')}
📍 *City:* {patient_data.get('city', 'N/A')}

🩺 *Symptoms:* {symptoms_str}
💓 *Vitals:* BP {patient_data.get('bp', 'N/A')} | Pulse {patient_data.get('pulse', 'N/A')} bpm

⚠️ *Predicted Condition:*
   {top_disease} ({top_prob}% probability)

📊 *Risk Score:* {risk['score']}/100 ({risk['category']})

🚨 *Risk Factors:*
{factors_str}

📞 *Action Required:* Immediate medical attention recommended

_Generated by Health Monitor System_
_Time: {patient_data.get('timestamp', 'N/A')}_"""
    
    return summary
