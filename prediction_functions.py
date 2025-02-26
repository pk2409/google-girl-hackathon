# parkinsons detection
input_data_parkinsons = [
    MDVP_Fo_Hz, MDVP_Fhi_Hz, MDVP_Flo_Hz, MDVP_Jitter_percent, MDVP_Jitter_Abs, 
    MDVP_RAP, MDVP_PPQ, Jitter_DDP, MDVP_Shimmer, MDVP_Shimmer_dB, 
    Shimmer_APQ3, Shimmer_APQ5, MDVP_APQ, Shimmer_DDA, NHR, HNR, RPDE, D2, 
    DFA, spread1, spread2, D2_duplicate, PPE
]

def predict_parkinsons(model_path, input_data_parkinsons):
    
    with open(model_path, "rb") as file:
        model = joblib.load(file)  
        print("Model loaded successfully!")

    input_array = np.asarray(input_data_parkinsons).reshape(1, -1)  
    prediction = model.predict(input_array)

    return int(prediction[0])  

# pancreatic cancer detection

input_data_pancreatic = [
    sample_id, patient_cohort, sample_origin, age, sex, diagnosis, stage, 
    benign_sample_diagnosis, plasma_CA19_9, creatinine
]
def predict_pancreatic_cancer(model_path, input_data_pancreatic):
    with open(model_path, "rb") as file:
        model = joblib.load(file)  
        print("Model loaded successfully!")

    input_array = np.asarray(input_data_pancreatic).reshape(1, -1)  
    prediction = model.predict(input_array)

    return int(prediction[0]) 

# asthma's disease 
input_data_asthma = [
    Tiredness, Dry_Cough, Difficulty_in_Breathing, Sore_Throat, None_Sympton, 
    Pains, Nasal_Congestion, Runny_Nose, None_Experiencing, Age_0_9
]
def predict_asthma(model_path, input_data_asthma):
    with open(model_path, "rb") as file:
        model = joblib.load(file)  
        print("Model loaded successfully!")

    input_array = np.asarray(input_data_asthma).reshape(1, -1)  
    prediction = model.predict(input_array)

    return int(prediction[0])


# alzheimer's disease
input_data_alzheimers = [
    patient_id, age, gender, ethnicity, education_level, bmi, smoking, 
    alcohol_consumption, physical_activity, diet_quality
]
def predict_alzheimers(model_path, input_data_alzheimers):
    with open(model_path, "rb") as file:
        model = joblib.load(file)  
        print("Model loaded successfully!")

    input_array = np.asarray(input_data_alzheimers).reshape(1, -1)  
    prediction = model.predict(input_array)

    return int(prediction[0])


# diabetes
input_data_diabetes = [
    Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, 
    DiabetesPedigreeFunction, Age
] 
def predict_diabetes(model_path, input_data_diabetes):
    with open(model_path, "rb") as file:
        model = joblib.load(file)  
        print("Model loaded successfully!")

    input_array = np.asarray(input_data_diabetes).reshape(1, -1)  
    prediction = model.predict(input_array)

    return int(prediction[0])


# thyroid detection
input_data_thyroid = [
    age, sex, on_thyroxine, query_on_thyroxine, on_antithyroid_medication, sick, 
    pregnant, thyroid_surgery, treatment, query_hypothyroid, query_hyperthyroid, 
    lithium, goitre, tumor, hypopituitary, psych, TSH_measured, TSH, 
    T3_measured, T3, TT4_measured, TT4, T4U_measured, T4U, FTI_measured, FTI, 
    TBG_measured, TBG, referral_source
]
def predict_thyroid(model_path, input_data_thyroid):
    with open(model_path, "rb") as file:
        model = joblib.load(file)  
        print("Model loaded successfully!")

    input_array = np.asarray(input_data_thyroid).reshape(1, -1)  
    prediction = model.predict(input_array)

    return int(prediction[0])



# kidney disease detection
input_data_ckd = [
    age, blood_pressure, specific_gravity, albumin, sugar, red_blood_cells, 
    pus_cell, pus_cell_clumps, bacteria, blood_glucose_random, blood_urea, 
    serum_creatinine, sodium, potassium, haemoglobin, packed_cell_volume, 
    white_blood_cell_count, red_blood_cell_count, hypertension, diabetes_mellitus, 
    coronary_artery_disease, appetite, peda_edema, aanemia, class_label
]

def predict_kidney_disease(model_path, input_data_ckd):
    with open(model_path, "rb") as file:
        model = joblib.load(file)  
        print("Model loaded successfully!")

    input_array = np.asarray(input_data_ckd).reshape(1, -1)  
    prediction = model.predict(input_array)

    return int(prediction[0])


# liver disease detection

input_data_liver = [
    Age, Gender, Total_Bilirubin, Direct_Bilirubin, Alkaline_Phosphotase, 
    Alamine_Aminotransferase, Aspartate_Aminotransferase, Total_Protiens, 
    Albumin, Albumin_and_Globulin_Ratio
]
def predict_liver_disease(model_path, input_data_liver):
    with open(model_path, "rb") as file:
        model = joblib.load(file)  
        print("Model loaded successfully!")

    input_array = np.asarray(input_data_liver).reshape(1, -1)  
    prediction = model.predict(input_array)

    return int(prediction[0])
