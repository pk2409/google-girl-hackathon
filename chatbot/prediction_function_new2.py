# liver disease detection

# ------------------------------> LIVER DISEASE <--------------------------------

def predict_liver_disease(model_path, input_data_liver):
    feature_names = [
    "Age", "Gender", "Total_Bilirubin", "Direct_Bilirubin", "Alkaline_Phosphotase", 
    "Alamine_Aminotransferase", "Aspartate_Aminotransferase", "Total_Protiens", 
    "Albumin", "Albumin_and_Globulin_Ratio"
]
    with open(model_path, "rb") as file:
        model = joblib.load(file)  
        print("Model loaded successfully!")

    input_array = np.asarray(input_data_liver).reshape(1, -1) 
    input_df = pd.DataFrame([input_data_liver], columns=feature_names) 
    prediction = model.predict(input_df)

    return int(prediction[0])

model_path = r'working-on-it\models\model_liver.pkl'  # Update this if the filename is different


# sample_input = [
#     100,  # Age
#      1,   # Gender (e.g., 1 for Male, 0 for Female)
#      1.2,  # Total Bilirubin
#         0.5,  # Direct Bilirubin
#         200,  # Alkaline Phosphotase
#         30,   # Alamine Aminotransferase
#         40,   # Aspartate Aminotransferase
#         6.5,  # Total Proteins
#         3.2,  # Albumin
#         1.1   # Albumin and Globulin Ratio
#     ]

#     # Run the test
# prediction = predict_liver_disease(model_path, sample_input)

#     # Print the result
# if prediction is not None:
#     if prediction == 2:
#         prediction = 0
# print("Predicted Class:", prediction)




# -------------------> ASTHMA PREDICTION <----------------
# def prediction_asthma(model_path, input_data_asthma):

import joblib
import pandas as pd
def predict_asthma(input_data_asthma):

    model_path = r'C:\Users\prish\Desktop\try3\working-on-it\models\model_asthma.pkl' 
    
    feature_names = [
    "Tiredness", "Dry-Cough", "Difficulty-in-Breathing", "Sore-Throat", "None_Sympton",
    "Pains", "Nasal-Congestion", "Runny-Nose", "None_Experiencing", "Age_0-9",
    "Age_10-19", "Age_20-24", "Age_25-59", "Age_60+", "Gender_Female", "Gender_Male"
]
    with open(model_path, "rb") as file:
        model = joblib.load(file)
        print("Asthma Model loaded successfully!")

    
    input_data_asthma = [input_data_asthma[feature] for feature in feature_names]
    input_df = pd.DataFrame([input_data_asthma], columns=feature_names)

    prediction = model.predict(input_df)

    return int(prediction[0])

 


# prediction = predict_asthma({"Tiredness": 1,
#     "Dry-Cough": 1,
#     "Difficulty-in-Breathing": 1,
#     "Sore-Throat": 0,
#     "None_Sympton": 0,
#     "Pains": 0,
#     "Nasal-Congestion": 1,
#     "Runny-Nose": 0,
#     "None_Experiencing": 0,
#     "Age_0-9": 1,
#     "Age_10-19": 0,
#     "Age_20-24": 0,
#     "Age_25-59": 0,
#     "Age_60+": 0,
#     "Gender_Female": 0,
#     "Gender_Male": 1})
# print("Predicted Class:", prediction)
    


# -------------> diabetes predictor <----------
import joblib
import pandas as pd
def predict_diabetes(input_data_diabetes):

    model_path = r'working-on-it\models\model_diabetes.pkl' 
    
    feature_names = ["Pregnancies",
        "Glucose",
        "BloodPressure",
        "SkinThickness",
        "Insulin",
        "BMI",
        "DiabetesPedigreeFunction",
        "Age"]
    
    with open(model_path, "rb") as file:
        model = joblib.load(file)
        print("Diabetes Model loaded successfully!")

    
    input_data_diabetes = [input_data_diabetes[feature] for feature in feature_names]
    input_df = pd.DataFrame([input_data_diabetes], columns=feature_names)

    prediction = model.predict(input_df)

    return int(prediction[0])


def predict_alzheimers(input_data_alzheimers):

    model_path = r'working-on-it\models\model_alzheimers.pkl' 
    
    feature_names = ["age",
        "gender",
        "ethnicity",
        "education_level",
        "bmi",
        "smoking",
        "alcohol_consumption",
        "physical_activity",
        "diet_quality"]
    
    with open(model_path, "rb") as file:
        model = joblib.load(file)
        print("Alzheimers Model loaded successfully!")

    
    input_data_alzheimers = [input_data_alzheimers[feature] for feature in feature_names]
    input_df = pd.DataFrame([input_data_alzheimers], columns=feature_names)

    prediction = model.predict(input_df)

    return int(prediction[0])



def predict_liver(input_data_liver):

    model_path = r'working-on-it\models\model_liver.pkl' 
    
    feature_names = ["Age",
        "Gender",
        "Total_Bilirubin",
        "Direct_Bilirubin",
        "Alkaline_Phosphotase",
        "Alamine_Aminotransferase",
        "Aspartate_Aminotransferase",
        "Total_Protiens",
        "Albumin",
        "Albumin_and_Globulin_Ratio"]
    
    with open(model_path, "rb") as file:
        model = joblib.load(file)
        print("Liver disease detection Model loaded successfully!")

    
    input_data_liver = [input_data_liver[feature] for feature in feature_names]
    input_df = pd.DataFrame([input_data_liver], columns=feature_names)

    prediction = model.predict(input_df)

    return int(prediction[0])


