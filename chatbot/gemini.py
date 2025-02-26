from google import genai
from google.genai import types
import numpy as np
import pandas as pd

conversation_history = []


MAX_TOKENS = 1000

ML_MODELS = {
    "SymptomClassifier": {
        "input_features": ["symptom_text", "duration_days", "severity_scale", "patient_age", "patient_gender"],
        "pred": lambda features: "Respiratory" if "cough" in features["symptom_text"].lower() else 
                                "Digestive" if "nausea" in features["symptom_text"].lower() else
                                "Neurological" if "headache" in features["symptom_text"].lower() else
                                "Cardiovascular" if "chest pain" in features["symptom_text"].lower() else
                                "General"
    },
    "DiagnosticPredictor": {
        "input_features": ["symptoms_list", "vital_signs", "patient_history", "age", "gender"],
        "pred": lambda features: {
            "primary": "Common Cold" if "cough" in features["symptoms_list"] and "runny nose" in features["symptoms_list"] else
                      "Migraine" if "headache" in features["symptoms_list"] and features.get("patient_history", "").lower().find("migraine") >= 0 else
                      "Gastritis" if "abdominal pain" in features["symptoms_list"] and "nausea" in features["symptoms_list"] else
                      "Hypertension" if features.get("vital_signs", {}).get("blood_pressure_systolic", 120) > 140 else
                      "Unknown",
            "confidence": 0.85,
            "alternatives": ["Flu", "Allergic Rhinitis", "Sinusitis"]
        }
    },
    "SeverityEstimator": {
        "input_features": ["symptoms", "duration", "progression_rate", "pain_level", "age"],
        "pred": lambda features: {
            "score": min(9, 1 + int(features.get("duration", 1)/2) + int(features.get("pain_level", 0))),
            "urgency": "High" if int(features.get("pain_level", 0)) > 7 else
                      "Medium" if int(features.get("pain_level", 0)) > 4 else
                      "Low"
        }
    },
    "TreatmentRecommender": {
        "input_features": ["diagnosis", "patient_age", "patient_gender", "medical_history", "current_medications"],
        "pred": lambda features: {
            "recommendations": [
                "Rest and hydration" if features["diagnosis"] in ["Common Cold", "Flu"] else None,
                "Over-the-counter pain relievers" if features["diagnosis"] in ["Headache", "Migraine", "Common Cold"] else None,
                "Prescription medication" if features["diagnosis"] in ["Hypertension", "Diabetes"] else None,
                "Lifestyle modifications" if features["diagnosis"] in ["Hypertension", "Obesity", "Diabetes"] else None,
                "Urgent medical attention" if features["diagnosis"] in ["Stroke", "Heart Attack"] else None
            ],
            "follow_up": "2 weeks" if features["diagnosis"] in ["Hypertension", "Diabetes"] else "As needed"
        }
    }
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
    global conversation_history
    
  
    conversation_history.append("User: " + user_input)
    
 
    conversation_history = trim_history(conversation_history, MAX_TOKENS)
    
 
    client = genai.Client(api_key="AIzaSyAAe-WQyIvOHdxAgB5AnqZ4BcGsoCBQG6c")
    
   
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
    
    Return your response in this format:
    {{
      "has_symptoms": true/false,
      "models_to_run": [
        {{
          "model_name": "ModelName",
          "feature_values": {{
            "feature1": "value1",
            "feature2": "value2",
            ...
          }}
        }},
        ...
      ],
      "direct_response": "Only include this if has_symptoms is false - your direct response to the user"
    }}
    """
    
    
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
    
    try:
        analysis = eval(response.text.strip())
        
        if analysis["has_symptoms"]:
            
            model_results = run_ml_models(analysis["models_to_run"])
            
           
            final_prompt = f"""
            Based on the following ML model predictions for the user's symptoms:
            
            User Input: "{user_input}"
            
            Model Predictions:
            {model_results}
            
            Provide a comprehensive medical assessment incorporating these predictions.
            Explain what each model is suggesting in plain language.
            Include any recommended next steps for the user.
            """
            
          
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
           
            assistant_reply = analysis["direct_response"]
    except Exception as e:
        
        print(e)
        assistant_reply = "I'm having trouble analyzing your input. Could you please provide more details about your symptoms or questions?"
    
    
    conversation_history.append("Assistant: " + assistant_reply)
    
    
    conversation_history = trim_history(conversation_history, MAX_TOKENS)
    
    return assistant_reply
