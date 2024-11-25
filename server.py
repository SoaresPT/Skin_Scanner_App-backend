from flask import Flask, request, jsonify
import onnxruntime as ort
import numpy as np
from skimage.io import imread
from skimage.transform import resize

# Load ONNX model
onnx_model_path = './model/model_2.onnx'
session = ort.InferenceSession(onnx_model_path)

# Prepare image for inference
def prepare_image(img):
    img = resize(img, (20, 20))  # Resizes image
    return img.flatten().astype(np.float32)

# Perform inference
def predict_image(img):
    input_data = prepare_image(img)
    # Prepare input for the model (matching the expected input name)
    input_name = session.get_inputs()[0].name
    output_name = session.get_outputs()[0].name
    # Run inference
    prediction = session.run([output_name], {input_name: input_data.reshape(1, -1)})  # Add batch dimension
    return prediction[0]

# Initialize Flask app
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided"}), 400
    file = request.files['image']
    if not file:
        return jsonify({"error": "No file uploaded"}), 400
    try:
        # Read the uploaded image
        img = imread(file.stream)
        prediction = predict_image(img)
        result = "Malignant" if prediction[0] == 1 else "Benign"
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)