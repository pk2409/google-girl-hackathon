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
    


