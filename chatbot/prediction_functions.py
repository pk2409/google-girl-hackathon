# parkinsons detection
# input_data_parkinsons = [
#     MDVP_Fo_Hz, MDVP_Fhi_Hz, MDVP_Flo_Hz, MDVP_Jitter_percent, MDVP_Jitter_Abs, 
#     MDVP_RAP, MDVP_PPQ, Jitter_DDP, MDVP_Shimmer, MDVP_Shimmer_dB, 
#     Shimmer_APQ3, Shimmer_APQ5, MDVP_APQ, Shimmer_DDA, NHR, HNR, RPDE, D2, 
#     DFA, spread1, spread2, D2_duplicate, PPE
# ]

# def predict_parkinsons(model_path, input_data_parkinsons):
    
#     with open(model_path, "rb") as file:
#         model = joblib.load(file)  
#         print("Model loaded successfully!")

#     input_array = np.asarray(input_data_parkinsons).reshape(1, -1)  
#     prediction = model.predict(input_array)

#     return int(prediction[0])  

# # pancreatic cancer detection

# input_data_pancreatic = [
#     sample_id, patient_cohort, sample_origin, age, sex, diagnosis, stage, 
#     benign_sample_diagnosis, plasma_CA19_9, creatinine
# ]
# def predict_pancreatic_cancer(model_path, input_data_pancreatic):
#     with open(model_path, "rb") as file:
#         model = joblib.load(file)  
#         print("Model loaded successfully!")

#     input_array = np.asarray(input_data_pancreatic).reshape(1, -1)  
#     prediction = model.predict(input_array)

#     return int(prediction[0]) 

# # asthma's disease 
# input_data_asthma = [
#     Tiredness, Dry_Cough, Difficulty_in_Breathing, Sore_Throat, None_Sympton, 
#     Pains, Nasal_Congestion, Runny_Nose, None_Experiencing, Age_0_9
# ]
# def predict_asthma(model_path, input_data_asthma):
#     with open(model_path, "rb") as file:
#         model = joblib.load(file)  
#         print("Model loaded successfully!")

#     input_array = np.asarray(input_data_asthma).reshape(1, -1)  
#     prediction = model.predict(input_array)

#     return int(prediction[0])


# # alzheimer's disease
# input_data_alzheimers = [
#     patient_id, age, gender, ethnicity, education_level, bmi, smoking, 
#     alcohol_consumption, physical_activity, diet_quality
# ]
# def predict_alzheimers(model_path, input_data_alzheimers):
#     with open(model_path, "rb") as file:
#         model = joblib.load(file)  
#         print("Model loaded successfully!")

#     input_array = np.asarray(input_data_alzheimers).reshape(1, -1)  
#     prediction = model.predict(input_array)

#     return int(prediction[0])


# # diabetes
# input_data_diabetes = [
#     Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, 
#     DiabetesPedigreeFunction, Age
# ] 
# def predict_diabetes(model_path, input_data_diabetes):
#     with open(model_path, "rb") as file:
#         model = joblib.load(file)  
#         print("Model loaded successfully!")

#     input_array = np.asarray(input_data_diabetes).reshape(1, -1)  
#     prediction = model.predict(input_array)

#     return int(prediction[0])


# # thyroid detection
# input_data_thyroid = [
#     age, sex, on_thyroxine, query_on_thyroxine, on_antithyroid_medication, sick, 
#     pregnant, thyroid_surgery, treatment, query_hypothyroid, query_hyperthyroid, 
#     lithium, goitre, tumor, hypopituitary, psych, TSH_measured, TSH, 
#     T3_measured, T3, TT4_measured, TT4, T4U_measured, T4U, FTI_measured, FTI, 
#     TBG_measured, TBG, referral_source
# ]
# def predict_thyroid(model_path, input_data_thyroid):
#     with open(model_path, "rb") as file:
#         model = joblib.load(file)  
#         print("Model loaded successfully!")

#     input_array = np.asarray(input_data_thyroid).reshape(1, -1)  
#     prediction = model.predict(input_array)

#     return int(prediction[0])



# # kidney disease detection
# input_data_ckd = [
#     age, blood_pressure, specific_gravity, albumin, sugar, red_blood_cells, 
#     pus_cell, pus_cell_clumps, bacteria, blood_glucose_random, blood_urea, 
#     serum_creatinine, sodium, potassium, haemoglobin, packed_cell_volume, 
#     white_blood_cell_count, red_blood_cell_count, hypertension, diabetes_mellitus, 
#     coronary_artery_disease, appetite, peda_edema, aanemia, class_label
# ]

# def predict_kidney_disease(model_path, input_data_ckd):
#     with open(model_path, "rb") as file:
#         model = joblib.load(file)  
#         print("Model loaded successfully!")

#     input_array = np.asarray(input_data_ckd).reshape(1, -1)  
#     prediction = model.predict(input_array)

#     return int(prediction[0])


# liver disease detection

# ------------------------------> LIVER DISEASE <--------------------------------
def prediction_liver(model_path,input_data_liver):
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

    model_path = r'C:\Users\prish\Desktop\try2_models\model_liver\model_liver.pkl'  # Update this if the filename is different


    sample_input = [
        100,  # Age
        1,   # Gender (e.g., 1 for Male, 0 for Female)
        1.2,  # Total Bilirubin
        0.5,  # Direct Bilirubin
        200,  # Alkaline Phosphotase
        30,   # Alamine Aminotransferase
        40,   # Aspartate Aminotransferase
        6.5,  # Total Proteins
        3.2,  # Albumin
        1.1   # Albumin and Globulin Ratio
    ]

    # Run the test
    prediction = predict_liver_disease(model_path, sample_input)

    # Print the result
    if prediction is not None:
        if prediction == 2:
            prediction = 0
    print("Predicted Class:", prediction)




# -------------------> ASTHMA PREDICTION <----------------
# def prediction_asthma(model_path, input_data_asthma):

import joblib
import pandas as pd
def predict_asthma(model_path, input_data_asthma):
    
    feature_names = [
    "Tiredness", "Dry-Cough", "Difficulty-in-Breathing", "Sore-Throat", "None_Sympton",
    "Pains", "Nasal-Congestion", "Runny-Nose", "None_Experiencing", "Age_0-9",
    "Age_10-19", "Age_20-24", "Age_25-59", "Age_60+", "Gender_Female", "Gender_Male"
]
    with open(model_path, "rb") as file:
        model = joblib.load(file)
        print("Asthma Model loaded successfully!")

    input_df = pd.DataFrame([input_data_asthma], columns=feature_names)
    prediction = model.predict(input_df)

    return int(prediction[0])

model_path = r'C:\Users\prish\Desktop\try2_models\model_asthma\model_asthma.pkl'  

sample_input = [1, 1, 1, 0, 0, 0, 1, 0, 0, 1,0,0,0,0,0,1]  
prediction = predict_asthma(model_path, sample_input)
print("Predicted Class:", prediction)
    




# -----------> KIDNEY DISEASE PREDICTION <-------------
# import joblib
# import pandas as pd
# def predict_asthma(model_path, input_data_asthma):
    
#     feature_names = ["age", "blood_pressure", "specific_gravity", "albumin", "sugar", "red_blood_cells", 
#      "pus_cell", "pus_cell_clumps", "bacteria", "blood_glucose_random", "blood_urea", 
#      "serum_creatinine", "sodium", "potassium", "haemoglobin", "packed_cell_volume", 
#      "white_blood_cell_count", "red_blood_cell_count", "hypertension", "diabetes_mellitus", 
#      "coronary_artery_disease", "appetite", "peda_edema", "aanemia"
    
# ]
#     with open(model_path, "rb") as file:
#         model = joblib.load(file)
#         print("Kidney disease detection Model loaded successfully!")

#     input_df = pd.DataFrame([input_data_asthma], columns=feature_names)
#     prediction = model.predict(input_df)

#     return int(prediction[0])

# model_path = r'C:\Users\prish\Desktop\try2_models\model_alzheimer\kidney_disease.pkl'  

# sample_input = [1, 1, 1, 0, 0, 0, 1, 0, 0, 1,0,0,0,0,0,1]  
# prediction = predict_asthma(model_path, sample_input)
# print("Predicted Class:", prediction)
    
