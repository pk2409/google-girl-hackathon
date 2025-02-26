# AI-Powered Diagnostic Assistant

## Overview
The AI-Powered Diagnostic Assistant is an intelligent chatbot-based system designed to assist in disease detection using both text-based symptom analysis and image-based medical scan evaluation. The system integrates multiple AI models to provide an accurate and data-driven diagnosis, reducing diagnostic errors and enhancing healthcare accessibility.

## Key Features
- **Text-Based Diagnosis:**
  - Users input symptoms.
  - The chatbot dynamically asks relevant follow-up questions.
  - The AI model predicts the most probable disease based on structured datasets.

- **Image-Based Diagnosis:**
  - Users upload medical scans (e.g., chest X-rays, MRI, CT scans).
  - A classification model identifies the type of scan.
  - The image is processed through a specialized deep learning model for disease detection.

- **Hybrid Analysis:**
  - Combines textual symptoms and image data for a more comprehensive diagnosis.

## Technologies Used
- **Natural Language Processing (NLP):** Gemini API for chatbot interaction.
- **Machine Learning (ML):** Supervised learning models trained on structured datasets.
- **Deep Learning (DL):** Convolutional Neural Networks (CNNs) for medical image classification.
- **Frameworks & Libraries:** TensorFlow, PyTorch, OpenCV, Pandas, NumPy, scikit-learn.

## System Architecture
1. **User Input Processing:**
   - If text-based, the chatbot asks follow-up questions based on disease models.
   - If image-based, the system detects the scan type and routes it to the appropriate model.

2. **Model Processing:**
   - Text input is classified using pre-trained models for disease prediction.
   - Image input is analyzed using CNN models tailored for different medical scans.

3. **Prediction & Diagnosis:**
   - The system provides a confidence score for potential diagnoses.
   - The results are displayed to the user along with recommendations.
  
  ## Implementation Steps
1. **Data Collection & Preprocessing:**
   - Gather structured medical datasets.
   - Clean and normalize data.
   - Perform feature selection.

2. **Model Training & Evaluation:**
   - Train ML models for text-based symptoms.
   - Train CNN models for medical images.
   - Evaluate accuracy using test datasets.

3. **Chatbot Development:**
   - Implement chatbot using Gemini API.
   - Integrate with backend for dynamic questioning.

4. **Integration & Deployment:**
   - Integrate ML models with chatbot
   - create workflow for specific input types
  
## Setup and Installation:
### 1. Prerequisites
Ensure you have the following installed:
- **Python 3.8+** (Download from [Python.org](https://www.python.org/downloads/))
- **pip (Python package manager)**

### 2. Create a Virtual Environment
```bash
# Create a virtual environment
python -m venv chatbot_env  

# Activate the virtual environment
# For Windows:
chatbot_env\Scripts\activate  
# For macOS/Linux:
source chatbot_env/bin/activate  
```

### 3. Install Required Dependencies
```bash
pip install streamlit gemini
```

### 4. Set Up API Key for Gemini
Get an API key from **Google Generative AI** and set it in your environment:
```bash
export GOOGLE_API_KEY="your_api_key_here"  # For macOS/Linux
set GOOGLE_API_KEY="your_api_key_here"  # For Windows
```

### 5. Run the Chatbot
```bash
streamlit run app.py
```
The chatbot UI will open in your browser.


## Supported Diseases & Models
1. **Pancreatic Cancer Detection**
   - Features:"sample_id",
        "patient_cohort",
        "sample_origin",
        "age",
        "sex",
        "diagnosis",
        "stage",
        "benign_sample_diagnosis",
        "plasma_CA19_9",
        "creatinine"


2. **Asthma Prediction**
   - Features: "Tiredness",
        "Dry-Cough",
        "Difficulty-in-Breathing",
        "Sore-Throat",
        "None_Sympton",
        "Pains",
        "Nasal-Congestion",
        "Runny-Nose",
        "None_Experiencing",
        "Age_0-9"


3. **Alzheimer’s Disease Prediction**
   - Features: "patient_id",
        "age",
        "gender",
        "ethnicity",
        "education_level",
        "bmi",
        "smoking",
        "alcohol_consumption",
        "physical_activity",
        "diet_quality"

4. **Diabetes Classification**
   - Features: "Pregnancies",
        "Glucose",
        "BloodPressure",
        "SkinThickness",
        "Insulin",
        "BMI",
        "DiabetesPedigreeFunction",
        "Age"

5. **Thyroid Disease Detection**
   - Features:  "age",
        "sex",
        "on thyroxine",
        "query on thyroxine",
        "on antithyroid medication",
        "sick",
        "pregnant",
        "thyroid surgery",
        "treatment",
        "query hypothyroid",
        "query hyperthyroid",
        "lithium",
        "goitre",
        "tumor",
        "hypopituitary",
        "psych",
        "TSH measured",
        "TSH",
        "T3 measured",
        "T3",
        "TT4 measured",
        "TT4",
        "T4U measured",
        "T4U",
        "FTI measured",
        "FTI",
        "TBG measured",
        "TBG",
        "referral source"


6. **Parkinson’s Disease Prediction**
   - Features: "MDVP:Fo(Hz)",
        "MDVP:Fhi(Hz)",
        "MDVP:Flo(Hz)",
        "MDVP:Jitter(%)",
        "MDVP:Jitter(Abs)",
        "MDVP:RAP",
        "MDVP:PPQ",
        "Jitter:DDP",
        "MDVP:Shimmer",
        "MDVP:Shimmer(dB)",
        "Shimmer:APQ3",
        "Shimmer:APQ5",
        "MDVP:APQ",
        "Shimmer:DDA",
        "NHR",
        "HNR",
        "RPDE",
        "D2",
        "DFA",
        "spread1",
        "spread2",
        "D2",
        "PPE"


7. **Chronic Kidney Disease Detection**
   - Features:"age",
        "blood_pressure",
        "specific_gravity",
        "albumin",
        "sugar",
        "red_blood_cells",
        "pus_cell",
        "pus_cell_clumps",
        "bacteria",
        "blood_glucose_random",
        "blood_urea",
        "serum_creatinine",
        "sodium",
        "potassium",
        "haemoglobin",
        "packed_cell_volume",
        "white_blood_cell_count",
        "red_blood_cell_count",
        "hypertension",
        "diabetes_mellitus",
        "coronary_artery_disease",
        "appetite",
        "peda_edema",
        "aanemia"


8. **Liver Disease Prediction**
   - Features:  "Age",
        "Gender",
        "Total_Bilirubin",
        "Direct_Bilirubin",
        "Alkaline_Phosphotase",
        "Alamine_Aminotransferase",
        "Aspartate_Aminotransferase",
        "Total_Protiens",
        "Albumin",
        "Albumin_and_Globulin_Ratio"





## Future Enhancements
- **Real-time Consultation:** Integrate with telemedicine services.
- **Expanded Disease Coverage:** Add more models for various health conditions.
- **User Data Security:** Implement end-to-end encryption for patient privacy.

## PROJECT IMPLEMENTATION FLOWCHART
  ![image](https://github.com/user-attachments/assets/da816fdc-96c3-4746-8983-3ee1f5f4183c)


## PROJECT PHASES 
![image](https://github.com/user-attachments/assets/2e8a3340-c38a-4600-9862-8464f5655f17)



## Conclusion
This AI-powered diagnostic assistant aims to revolutionize early disease detection, offering scalable, data-driven, and cost-effective healthcare solutions. It bridges gaps in healthcare accessibility and empowers both patients and medical professionals with reliable diagnostic insights.
