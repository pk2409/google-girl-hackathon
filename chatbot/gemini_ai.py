# import google.generativeai as genai

from prediction_function_new import predict_liver , predict_asthma , predict_diabetes , predict_alzheimers



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

# Maximum token limit
MAX_TOKENS = 1000






# -----------------> defining different portions of our code <---------------
ML_MODELS = {
    "Asthma_Predictor": {
        "input_features": [
    "Tiredness", "Dry-Cough", "Difficulty-in-Breathing", "Sore-Throat", "None_Sympton",
    "Pains", "Nasal-Congestion", "Runny-Nose", "None_Experiencing", "Age_0-9",
    "Age_10-19", "Age_20-24", "Age_25-59", "Age_60+", "Gender_Female", "Gender_Male"
],
        "pred": lambda features: predict_asthma({
    "Tiredness": 1,
    "Dry-Cough": 1,
    "Difficulty-in-Breathing": 1,
    "Sore-Throat": 0,
    "None_Sympton": 0,
    "Pains": 0,
    "Nasal-Congestion": 1,
    "Runny-Nose": 0,
    "None_Experiencing": 0,
    "Age_0-9": 1,
    "Age_10-19": 0,
    "Age_20-24": 0,
    "Age_25-59": 0,
    "Age_60+": 0,
    "Gender_Female": 0,
    "Gender_Male": 1
})
    },
    "Diabetes_predictor": {
        "input_features": [
        "Pregnancies",
        "Glucose",
        "BloodPressure",
        "SkinThickness",
        "Insulin",
        "BMI",
        "DiabetesPedigreeFunction",
        "Age"
      ],  # Use disease-specific feature mapping
        "pred": lambda features: predict_diabetes({
    "Pregnancies": 2,
    "Glucose": 140,
    "BloodPressure": 80,
    "SkinThickness": 20,
    "Insulin": 90,
    "BMI": 30.0,
    "DiabetesPedigreeFunction": 0.5,
    "Age": 45
})  
    },
    "Alzheimers_Predictor": {
        "input_features": [
        "age",
        "gender",
        "ethnicity",
        "education_level",
        "bmi",
        "smoking",
        "alcohol_consumption",
        "physical_activity",
        "diet_quality"],
        "pred": lambda features: predict_alzheimers({"age": 35,
    "gender": "Female",
    "ethnicity": "Caucasian",
    "education_level": "Bachelor's Degree",
    "bmi": 25.5,
    "smoking": "Non-smoker",
    "alcohol_consumption": "Moderate",
    "physical_activity": "Regular",
    "diet_quality": "Good" 
    })
    },
    "Liver_Disease_Predictor": {
        "input_features": ["Age",
        "Gender",
        "Total_Bilirubin",
        "Direct_Bilirubin",
        "Alkaline_Phosphotase",
        "Alamine_Aminotransferase",
        "Aspartate_Aminotransferase",
        "Total_Protiens",
        "Albumin",
        "Albumin_and_Globulin_Ratio"],
        "pred": lambda features: predict_liver({"Age": 50,
    "Gender": "Male",
    "Total_Bilirubin": 1.2,
    "Direct_Bilirubin": 0.3,
    "Alkaline_Phosphotase": 85,
    "Alamine_Aminotransferase": 35,
    "Aspartate_Aminotransferase": 30,
    "Total_Protiens": 6.8,
    "Albumin": 4.2,
    "Albumin_and_Globulin_Ratio": 1.2})
    }
}







# -----------> which variables to run <-------------

# def predict_disease_from_category(category, input_data):
#     if category not in CATEGORY_TO_DISEASES:
#         return {"error": "Unknown category"}
    
#     possible_diseases = CATEGORY_TO_DISEASES[category]
#     results = {}

#     for disease in possible_diseases:
#         model_path = MODEL_PATHS.get(disease, None)
#         if model_path:
#             results[disease] = predict_disease(disease, model_path, input_data)

#     # Select the most confident result (if applicable)
#     best_diagnosis = max(results, key=lambda d: results[d]["confidence"], default="Unknown")

#     return {"diagnosis": best_diagnosis, "details": results}





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
    
    # Add user input to conversation history
    conversation_history.append("User: " + user_input)
    
    # Trim history to stay within token limits
    conversation_history = trim_history(conversation_history, MAX_TOKENS)



    if pending_features:
            # Assume one model is pending at a time
            current_model = list(pending_features.keys())[0]
            features_pending = pending_features[current_model]
            
            # Determine the next missing feature (i.e. one with empty value)
            for feature, value in features_pending.items():
                if value is None or value == "":
                    # Update the pending feature with the user's answer
                    features_pending[feature] = user_input.strip()
                    break
            
            # Check if all missing features have been provided
            if all(v is not None and v != "" for v in features_pending.values()):
                # All required features for current_model have been provided.
                # Create a model selection dictionary to run the model.
                model_selection = [{
                    "model_name": current_model,
                    "feature_values": features_pending
                }]
                # Run the model
                model_result = run_ml_models(model_selection)
                # Clear pending features for the current model
                pending_features.pop(current_model)
                reply = f"Prediction for {current_model}: {model_result[current_model]}"
                conversation_history.append("Assistant: " + reply)
                conversation_history = trim_history(conversation_history, MAX_TOKENS)
                return reply
            else:
                # Still missing some features; ask for the next missing feature.
                for feature, value in features_pending.items():
                    if value is None or value == "":
                        reply = f"Please provide the value for '{feature}' for {current_model}."
                        conversation_history.append("Assistant: " + reply)
                        conversation_history = trim_history(conversation_history, MAX_TOKENS)
                        return reply
    
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
        
        if analysis["has_symptoms"]:
            # Run the ML models with the provided feature values
            model_results = run_ml_models(analysis["models_to_run"])
            
            # Construct a prompt for the final medical response
            final_prompt = f"""
            Based on the following ML model predictions for the user's symptoms:
            
            User Input: "{user_input}"
            
            Model Predictions:
            {model_results}
            
            Provide a comprehensive medical assessment incorporating these predictions.
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