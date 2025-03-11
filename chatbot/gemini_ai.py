# import google.generativeai as genai

from prediction_function_new2 import predict_liver , predict_asthma , predict_diabetes , predict_alzheimers



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
models_to_run = []
# Maximum token limit
MAX_TOKENS = 1000






# -----------------> defining different portions of our code <---------------
ML_MODELS = {
    "Asthma_Predictor": {
        "input_features": [
     ["Tiredness", "int"],
    ["Dry-Cough", "int"],
    ["Difficulty-in-Breathing", "int"],
    ["Sore-Throat", "int"],
    ["None_Sympton", "int"],
    ["Pains", "int"],
    ["Nasal-Congestion", "int"],
    ["Runny-Nose", "int"],
    ["None_Experiencing", "int"],
    ["Age_0-9", "int"],
    ["Age_10-19", "int"],
    ["Age_20-24", "int"],
    ["Age_25-59", "int"],
    ["Age_60+", "int"],
    ["Gender_Female", "int"],
    ["Gender_Male", "int"]
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
         ["Pregnancies", "int"],
    ["Glucose", "int"],
    ["BloodPressure", "int"],
    ["SkinThickness", "int"],
    ["Insulin", "int"],
    ["BMI", "float"],
    ["DiabetesPedigreeFunction", "float"],
    ["Age", "int"]
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
         ["age", "int"],
    ["gender", "str"],
    ["ethnicity", "str"],
    ["education_level", "str"],
    ["bmi", "float"],
    ["smoking", "str"],
    ["alcohol_consumption", "str"],
    ["physical_activity", "str"],
    ["diet_quality", "str"]],
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
        "input_features": [["Age", "int"],
    ["Gender", "str"],
    ["Total_Bilirubin", "float"],
    ["Direct_Bilirubin", "float"],
    ["Alkaline_Phosphotase", "int"],
    ["Alamine_Aminotransferase", "int"],
    ["Aspartate_Aminotransferase", "int"],
    ["Total_Protiens", "float"],
    ["Albumin", "float"],
    ["Albumin_and_Globulin_Ratio", "float"]],
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
    global conversation_history, features , models_to_run
    
    # Add user input to conversation history
    conversation_history.append("User: " + user_input)
    
    # Trim history to stay within token limits
    conversation_history = trim_history(conversation_history, MAX_TOKENS)
    # Initialize Gemini client
    client = genai.Client(api_key="AIzaSyAAe-WQyIvOHdxAgB5AnqZ4BcGsoCBQG6c")
    ML = {}
    for m in models_to_run:
        ML[m]=ML_MODELS[m]
    if not ML:
        ML= ML_MODELS
    # Construct the main prompt that does most of the work
    main_prompt = f"""
    Based on the following prompt, check whether the user is listing medical symptoms or not:
    
    User input: "{user_input}"
    
    If the user is NOT listing symptoms, return a reply as a medical professional that asks clarifying questions.
    
    If the user IS listing symptoms, identify those symptoms and check which of the following ML models they can be used with:
    
    {ML}
    I already have some features do not add these:
    {features}
    
    For each applicable model, return:
    1. The model name
    2. A list of feature values that can be extracted from the user's input
    3. Default values for any missing required features
    4. key of features is to be taken from ML_MODELS
    5. Do not add any extra keys
    6. Do not assume features that the user can aswer
    7. append all features/symtoms inside the key features do not make a new key nomaed on the model_name
    Return your response in this format:
    {{
      "has_symptoms": true/false,

      "models_to_run": [
         "ModelName",
        ...
      ],
      "features": {{
        "feature1": "extracted_value1",
        "feature2": "extracted_value2",
        ...
      }},
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
            print(features)
            models_to_run=analysis["models_to_run"]
            ask_features= list()
            for model in analysis["models_to_run"]:
                print(model)
                print(ML_MODELS[model]["input_features"])
                for f in ML_MODELS[model]["input_features"]:
                    # print(f[0])
                    if f[0] not in features:
                        ask_features.append(f[0])
            print(99)
            for model_name, model_info in ML_MODELS.items():
                required_features = model_info.get("input_features", [])
                all_features_present = True
                for feature in required_features:
                    if feature[0] not in features:
                        all_features_present = False
                        break

                if(all_features_present):
                    model_selection = {
                        "model_name": model_name,
                        "feature_values": {feature[0]: features[feature[0]] for feature in required_features}
                    }
                    runnable_models.append(model_selection)
                    models_to_run.remove(model_name)
                    try:
                        models_to_run.remove(model_name)
                    except ValueError:
                        print(ValueError)
            print(1)
            # Run the ML models with the provided feature values
            print(runnable_models)
            model_results = run_ml_models(runnable_models)
            print(model_results)
            # Construct a prompt for the final medical response
            final_prompt = f"""
            Based on the following ML model predictions for the user's symptoms:
            
            User Input: "{user_input}"
        
            Pending Features:
            "{ask_features}"

            Model Predictions:
            {model_results}
            If Features to be asked is not empty then frame a reply to ask the question to get the features from the user.
            Do not use bold,italics or special characters in the response

            and then Provide a comprehensive medical assessment incorporating these predictions.
            Explain what each model is suggesting in plain language.
            Include any recommended next steps for the user.
            NOTE:
            1. do not list symptoms that are already answered until necessay.
            2. return in a frmat no ***
            3. you can use \\n to format it in a better way as it will be printed
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
