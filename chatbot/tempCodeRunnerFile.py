import joblib
import pandas as pd
import numpy as np

def predict_parkinsons(model_path, input_data_parkinsons):
    feature_names = [
        "MDVP_Fo_Hz", "MDVP_Fhi_Hz", "MDVP_Flo_Hz", "MDVP_Jitter_percent", "MDVP_Jitter_Abs",
        "MDVP_RAP", "MDVP_PPQ", "Jitter_DDP", "MDVP_Shimmer", "MDVP_Shimmer_dB",
        "Shimmer_APQ3", "Shimmer_APQ5", "MDVP_APQ", "Shimmer_DDA", "NHR", "HNR", "RPDE", "D2",
        "DFA", "spread1", "spread2", "D2_duplicate", "PPE"
    ]

    with open(model_path, "rb") as file:
        model = joblib.load(file)
        print("Parkinson’s Model loaded successfully!")

    input_df = pd.DataFrame([input_data_parkinsons], columns=feature_names)
    prediction = model.predict(input_df)

    return int(prediction[0])

# Example usage
model_path = r'C:\Users\prish\Downloads\model7.h5'  

sample_input = [120.0, 140.0, 100.0, 0.002, 0.00002, 0.001, 0.002, 0.003, 0.02, 0.3, 
                0.01, 0.015, 0.017, 0.022, 0.1, 20.5, 0.4, 2.1, 0.7, -4.5, 0.2, 2.3, 0.05]  

prediction = predict_parkinsons(model_path, sample_input)
print("Predicted Class:", prediction)
