# This is a draft... Will be updated thoroughly after deployment
# Skin Scanner App Backend

This project is a Flask-based web application for image classification using an ONNX model. Given an input image, the application predicts whether the image is classified as "Malignant" or "Benign".

## Prerequisites

Before you can run this application, you'll need to have the following installed on your machine:

- Python 3.x
- pip

## Installation

Follow these steps to set up the project:

1. **Clone the Repository**

   Clone the repository to your local machine:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a Virtual Environment**

   Setting up a virtual environment is a good practice to keep dependencies organized:

   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**

   - On Windows:

     ```bash
     .\venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install Required Packages**

   Once the virtual environment is activated, install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

   If `requirements.txt` doesn't exist yet, you can create it with the following content:

   ```plaintext
   Flask
   onnxruntime
   scikit-image
   ```

5. **Place the ONNX Model**

   Make sure your ONNX model is located at `./model/model_2.onnx`.

## Running the Application

To start the Flask application, use the following command:

```bash
python app.py
```

This will start the server on `http://0.0.0.0:8000`.

## Usage

To perform an inference, send a POST request to the `/predict` endpoint with an image file:

- **Endpoint:** `/predict`
- **Method:** `POST`
- **Form Data:** Image file with the key as `image`.

### Example Request with Python

You can test the API using Python's `requests` module as follows:

```python
import requests

# URL of the Flask server
url = 'http://0.0.0.0:8000/predict'

# Path to the sample image
image_path = 'path/to/your/image.jpg'

# Send a POST request with the image file
with open(image_path, 'rb') as img_file:
    files = {'image': img_file}
    response = requests.post(url, files=files)

# Print the response from the server
print(response.json())
```

## Error Handling

The application returns error messages for the following cases:

- No image file provided: Returns a 400 status code with an error message.
- No file uploaded: Returns a 400 status code with an error message.
- Unexpected errors: Returns a 500 status code with a detailed error message.

## Running the Application

Start the Flask server:

```bash
python server.py
```

Then, to test the API, run:

```bash
python test_api.py
```

Ensure to update the `test_api.py` file with the correct path to your test image before executing it.

## Testing with cURL

```bash
curl -X POST -F "image=@path/to/your/image.jpg" http://0.0.0.0:8000/predict
```