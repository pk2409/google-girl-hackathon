import tensorflow as tf
import numpy as np
from PIL import Image

image_classifier = tf.keras.models.load_model("models/image_classifier.h5")

MODELS = {
    "lung_scan": ["models/covid_model.h5", "models/pneumonia_model.h5"],
    "brain_mri": ["models/brain_tumor_model.h5"],
}

def predict_image_type(image):
    image = image.resize((224, 224)) 
    image_array = np.array(image) / 255.0 
    image_array = np.expand_dims(image_array, axis=0) 
    
    prediction = image_classifier.predict(image_array)
    labels = ["lung_scan", "brain_mri"]  
    return labels[np.argmax(prediction)]

def load_models(model_paths):
    return [tf.keras.models.load_model(path) for path in model_paths]

def process_image_through_models(image, model_paths):
    models = load_models(model_paths)
    results = {}

    for model_path, model in zip(model_paths, models):
        image_array = np.expand_dims(np.array(image) / 255.0, axis=0)
        result = model.predict(image_array)
        results[model_path] = result.tolist()

    return results
