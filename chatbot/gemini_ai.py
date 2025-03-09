# import google.generativeai as genai

from prediction_functions import prediction_liver


from google import genai
# import google.generativeai as genai
from google.genai import types


import numpy as np
import pandas as pd
import json

# Initialize conversation history
pending_features = {}  # Stores missing features for each user
collected_feature_values = {}  # Stores collected values
conversation_history = []
features={}
# Maximum token limit
MAX_TOKENS = 1000

# Define ML models with their prediction functions
# ML_MODELS = {
#     "SymptomClassifier": {
#         "input_features": ["symptom_text", "duration_days", "severity_scale", "patient_age", "patient_gender"],
#         "pred": lambda features: "Respiratory" if "cough" in features["symptom_text"].lower() else 
#                                 "Digestive" if "nausea" in features["symptom_text"].lower() else
#                                 "Neurological" if "headache" in features["symptom_text"].lower() else
#                                 "Cardiovascular" if "chest pain" in features["symptom_text"].lower() else
#                                 "General"
#     },
#     "DiagnosticPredictor": {
#         "input_features": ["symptoms_list", "vital_signs", "patient_history", "age", "gender"],
#         "pred": lambda features: {
#             "primary": "Common Cold" if "cough" in features["symptoms_list"] and "runny nose" in features["symptoms_list"] else
#                       "Migraine" if "headache" in features["symptoms_list"] and features.get("patient_history", "").lower().find("migraine") >= 0 else
#                       "Gastritis" if "abdominal pain" in features["symptoms_list"] and "nausea" in features["symptoms_list"] else
#                       "Hypertension" if features.get("vital_signs", {}).get("blood_pressure_systolic", 120) > 140 else
#                       "Unknown",
#             "confidence": 0.85,
#             "alternatives": ["Flu", "Allergic Rhinitis", "Sinusitis"]
#         }
#     },
#     "SeverityEstimator": {
#         "input_features": ["symptoms", "duration", "progression_rate", "pain_level", "age"],
#         "pred": lambda features: {
#             "score": min(9, 1 + int(features.get("duration", 1)/2) + int(features.get("pain_level", 0))),
#             "urgency": "High" if int(features.get("pain_level", 0)) > 7 else
#                       "Medium" if int(features.get("pain_level", 0)) > 4 else
#                       "Low"
#         }
#     },
#     "TreatmentRecommender": {
#         "input_features": ["diagnosis", "patient_age", "patient_gender", "medical_history", "current_medications"],
#         "pred": lambda features: {
#             "recommendations": [
#                 "Rest and hydration" if features["diagnosis"] in ["Common Cold", "Flu"] else None,
#                 "Over-the-counter pain relievers" if features["diagnosis"] in ["Headache", "Migraine", "Common Cold"] else None,
#                 "Prescription medication" if features["diagnosis"] in ["Hypertension", "Diabetes"] else None,
#                 "Lifestyle modifications" if features["diagnosis"] in ["Hypertension", "Obesity", "Diabetes"] else None,
#                 "Urgent medical attention" if features["diagnosis"] in ["Stroke", "Heart Attack"] else None
#             ],
#             "follow_up": "2 weeks" if features["diagnosis"] in ["Hypertension", "Diabetes"] else "As needed"
#         }
#     }
# }

DISEASE_FEATURES = {
    "parkinsons": ["MDVP_Fo_Hz", "MDVP_Fhi_Hz", "MDVP_Flo_Hz", "MDVP_Jitter_percent", 
                   "MDVP_Jitter_Abs", "MDVP_RAP", "MDVP_PPQ", "Jitter_DDP", "MDVP_Shimmer", 
                   "MDVP_Shimmer_dB", "Shimmer_APQ3", "Shimmer_APQ5", "MDVP_APQ", 
                   "Shimmer_DDA", "NHR", "HNR", "RPDE", "D2", "DFA", "spread1", "spread2", 
                   "D2_duplicate", "PPE"],
                   
    "pancreatic_cancer": ["sample_id", "patient_cohort", "sample_origin", "age", "sex", 
                          "diagnosis", "stage", "benign_sample_diagnosis", "plasma_CA19_9", 
                          "creatinine"],

    "asthma": ["Tiredness", "Dry_Cough", "Difficulty_in_Breathing", "Sore_Throat", 
               "None_Sympton", "Pains", "Nasal_Congestion", "Runny_Nose", "None_Experiencing", 
               "Age_0_9"],

    "alzheimers": ["patient_id", "age", "gender", "ethnicity", "education_level", "bmi", 
                   "smoking", "alcohol_consumption", "physical_activity", "diet_quality"],

    "diabetes": ["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin", 
                 "BMI", "DiabetesPedigreeFunction", "Age"],

    "thyroid": ["age", "sex", "on_thyroxine", "query_on_thyroxine", "on_antithyroid_medication", 
                "sick", "pregnant", "thyroid_surgery", "treatment", "query_hypothyroid", 
                "query_hyperthyroid", "lithium", "goitre", "tumor", "hypopituitary", "psych", 
                "TSH_measured", "TSH", "T3_measured", "T3", "TT4_measured", "TT4", 
                "T4U_measured", "T4U", "FTI_measured", "FTI", "TBG_measured", "TBG", 
                "referral_source"],

    "kidney_disease": ["age", "blood_pressure", "specific_gravity", "albumin", "sugar", 
                       "red_blood_cells", "pus_cell", "pus_cell_clumps", "bacteria", 
                       "blood_glucose_random", "blood_urea", "serum_creatinine", "sodium", 
                       "potassium", "haemoglobin", "packed_cell_volume", 
                       "white_blood_cell_count", "red_blood_cell_count", "hypertension", 
                       "diabetes_mellitus", "coronary_artery_disease", "appetite", 
                       "peda_edema", "aanemia", "class_label"],

    "liver_disease": ["Age", "Gender", "Total_Bilirubin", "Direct_Bilirubin", 
                      "Alkaline_Phosphotase", "Alamine_Aminotransferase", 
                      "Aspartate_Aminotransferase", "Total_Protiens", "Albumin", 
                      "Albumin_and_Globulin_Ratio"]
}



# -----------------> defining different portions of our code <---------------
ML_MODELS = {
    "Asthma": {
        "input_features": ["Tiredness", "Dry-Cough", "Difficulty-in-Breathing", "Sore-Throat", "None_Sympton",
    "Pains", "Nasal-Congestion", "Runny-Nose", "None_Experiencing", "Age_0-9",
    "Age_10-19", "Age_20-24", "Age_25-59", "Age_60+", "Gender_Female", "Gender_Male"],
        "pred": lambda features: classify_disease(features)  # Replace with function
    },
    "DiseasePredictor": {
        "input_features": DISEASE_FEATURES,  # Use disease-specific feature mapping
        "pred": lambda disease_name, features: predict_disease(disease_name, MODEL_PATHS[disease_name], features)  
    },
    "SeverityEstimator": {
        "input_features": ["symptoms", "duration", "progression_rate", "pain_level", "age"],
        "pred": lambda features: estimate_severity(features)
    },
    "TreatmentRecommender": {
        "input_features": ["diagnosis", "patient_age", "patient_gender", "medical_history", "current_medications"],
        "pred": lambda features: recommend_treatment(features)
    }
}



# -------------------> classification = which disease type <-------------------


def classify_disease(features):
    symptom_text = features["symptom_text"].lower()
    
    if any(word in symptom_text for word in ["cough", "cold", "breath"]):
        return "Respiratory"
    elif any(word in symptom_text for word in ["nausea", "stomach ache"]) :
        return "Digestive"
    elif "headache" in symptom_text:
        return "Neurological"
    elif "chest pain" in symptom_text:
        return "Cardiovascular"
    else:
        return "General"



# ----------> which disease which function to run for prediction <-----------------

def predict_disease(disease_name, model_path, input_data):
    disease_mapping = {
        "parkinsons": predict_parkinsons,
        "pancreatic_cancer": predict_pancreatic_cancer,
        "asthma": predict_asthma,
        "alzheimers": predict_alzheimers,
        "diabetes": predict_diabetes,
        "thyroid": predict_thyroid,
        "kidney_disease": predict_kidney_disease,
        "liver_disease": prediction_liver
    }

    if disease_name in disease_mapping:
        return disease_mapping[disease_name](model_path, input_data)
    return "Error: Disease not recognized"




# ------------> category specific which diseases  <---------------

CATEGORY_TO_DISEASES = {
    "Respiratory": ["asthma"],
    "Digestive": ["pancreatic_cancer", "liver_disease"],
    "Neurological": ["parkinsons", "alzheimers"],
    "Cardiovascular": ["hypertension"],
    "General": ["diabetes", "thyroid", "kidney_disease"]
}


# -----------> which variables to run <-------------

def predict_disease_from_category(category, input_data):
    if category not in CATEGORY_TO_DISEASES:
        return {"error": "Unknown category"}
    
    possible_diseases = CATEGORY_TO_DISEASES[category]
    results = {}

    for disease in possible_diseases:
        model_path = MODEL_PATHS.get(disease, None)
        if model_path:
            results[disease] = predict_disease(disease, model_path, input_data)

    # Select the most confident result (if applicable)
    best_diagnosis = max(results, key=lambda d: results[d]["confidence"], default="Unknown")

    return {"diagnosis": best_diagnosis, "details": results}



# -----------> all model paths <----------
MODEL_PATHS = {
    "parkinsons": "path/to/parkinsons_model.pkl",
    "pancreatic_cancer": "path/to/pancreatic_model.pkl",
    "asthma": "path/to/asthma_model.pkl",
    "alzheimers": "path/to/alzheimers_model.pkl",
    "diabetes": "path/to/diabetes_model.pkl",
    "thyroid": "path/to/thyroid_model.pkl",
    "kidney_disease": "path/to/kidney_model.pkl",
    "liver_disease": "path/to/liver_model.pkl"
}



def count_tokens(text: str) -> int:
    """Count tokens in the text (simplified)"""
    return len(text.split())

def trim_history(history: list, max_tokens: int) -> list:
    """Trim conversation history to stay within token limit"""
    while history and count_tokens("\n".join(history)) > max_tokens and len(history) > 1:
        history.pop(0)
    return history

def run_ml_models(model_selections):
    """Run the selected ML models with the provided feature values"""
    results = {}
    
    for model_info in model_selections:
        model_name = model_info["model_name"]
        feature_values = model_info["feature_values"]
        
        if model_name in ML_MODELS:
            # Run the prediction function for this model
            try:
                prediction = ML_MODELS[model_name]["pred"](feature_values)
                results[model_name] = prediction
            except Exception as e:
                results[model_name] = {"error": str(e)}
        else:
            results[model_name] = {"error": "Model not found"}
    
    return results

def get_response(user_input: str) -> str:
    """Process user input and generate appropriate response"""
    global conversation_history, features
    
    # Add user input to conversation history
    conversation_history.append("User: " + user_input)
    
    # Trim history to stay within token limits
    conversation_history = trim_history(conversation_history, MAX_TOKENS)
    # Initialize Gemini client
    client = genai.Client(api_key="AIzaSyAAe-WQyIvOHdxAgB5AnqZ4BcGsoCBQG6c")
    
    # Construct the main prompt that does most of the work
    main_prompt = f"""
    Based on the following prompt, check whether the user is listing medical symptoms or not:
    
    User input: "{user_input}"
    
    If the user is NOT listing symptoms, return a reply as a medical professional that asks clarifying questions.
    
    If the user IS listing symptoms, identify those symptoms and check which of the following ML models they can be used with:
    
    {ML_MODELS}
    
    For each applicable model, return:
    1. The model name
    2. A list of feature values that can be extracted from the user's input
    3. Default values for any missing required features
    4. key of features is to be taken from ML_MODELS

     For features_to_be_asked, include only features that:
    1. Are required by at least one ML model
    2. Cannot be determined from the user's input
    3. Are reasonable for the user to know without medical testing

    Return your response in this format:
    {{
      "has_symptoms": true/false,

      "models_to_run": [
        {{
          "model_name": "ModelName",
        }},
        ...
      ],
      "features": {{
        "feature1": "extracted_value1",
        "feature2": "extracted_value2",
        ...
      }},
      "ask_for_more_data": "Yes/No",
      "features_to_be_asked": ["feature3", "feature4", ...],
      "direct_response": "Only include this if has_symptoms is false - your direct response to the user"
    }}
    """
    
    # Get the response from Gemini
    sys_instruct = (
        "You are a medical assistant that can analyze symptoms and determine which ML models to use. "
        "Be precise in extracting symptoms and matching them to appropriate models."
    )
    
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[main_prompt],
        config=types.GenerateContentConfig(
            system_instruction=sys_instruct,
            max_output_tokens=800,
            temperature=0.1
        )
    )
    print(response)
    # Parse the response
    try:
        #analysis = eval(response.text.strip())
        response_text = response.candidates[0].content.parts[0].text.strip()
    
    # Remove code block markers if present
        if response_text.startswith("```json") and response_text.endswith("```"):
            response_text = response_text[7:-3].strip()
        
        analysis = json.loads(response_text)
        features.update(analysis.get("features", {}))
        runnable_models = []
        if analysis["has_symptoms"]:
            print("here")
            print(analysis)
            for model_name, model_info in ML_MODELS.items():
                required_features = model_info.get("input_features", [])
                if all(feature in features and features[feature] for feature in required_features):
                    model_selection = {
                        "model_name": model_name,
                        "feature_values": {feature: features[feature] for feature in required_features}
                    }
                    runnable_models.append(model_selection)
            print(1)
            # Run the ML models with the provided feature values
            model_results = run_ml_models(runnable_models)
            print(2)
            # Construct a prompt for the final medical response
            final_prompt = f"""
            Based on the following ML model predictions for the user's symptoms:
            
            User Input: "{user_input}"
        
            Pending Features:
            "{analysis["features_to_be_asked"]}"

            Model Predictions:
            {model_results}
            If Features to be asked is not empty then frame a reply to ask the question to get the features from the user.
            and then Provide a comprehensive medical assessment incorporating these predictions.
            Explain what each model is suggesting in plain language.
            Include any recommended next steps for the user.
            """
            
            # Get the final medical response
            final_response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=[final_prompt],
                config=types.GenerateContentConfig(
                    system_instruction="You are a helpful medical professional providing advice based on ML model predictions.",
                    max_output_tokens=500,
                    temperature=0.1
                )
            )
            
            assistant_reply = final_response.text.strip()
        else:
            print("2")
            print("3")
            print("4")
            # Use the direct response from the first call
            assistant_reply = analysis["direct_response"]
    except Exception as e:
        # Fallback in case of parsing errors
        print(e)
        assistant_reply = "I'm having trouble analyzing your input. Could you please provide more details about your symptoms or questions?"
    
    # Add assistant reply to conversation history
    conversation_history.append("Assistant: " + assistant_reply)
    
    # Trim history again
    conversation_history = trim_history(conversation_history, MAX_TOKENS)
    
    return assistant_reply