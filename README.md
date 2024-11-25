# Skin Scanner App Backend

This project is a Flask-based web application for image classification using an ONNX model. Given an input image, the application predicts whether the image is classified as "Malignant" or "Benign".

## Prerequisites

To run this application locally, ensure the following are installed on your machine:

- Python 3.10
- pip

## Installation

Follow these steps to set up the project locally:

1. **Clone the Repository**

   Clone the repository to your machine:

   ```bash
   git clone https://github.com/SoaresPT/Skin_Scanner_App-backend.git
   cd Skin_Scanner_App-backend
   ```

2. **Create a Virtual Environment**

   Set up a virtual environment to manage dependencies:

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

   With the virtual environment activated, install the necessary Python packages:

   ```bash
   pip install -r requirements.txt
   ```

5. **ONNX Model**

   ONNX models should be placed inside `model`. Currently defaults to:  `./model/model_2.onnx`.

## Running the Application Locally

To start the Flask application:

```bash
python server.py
```

The server will be accessible at `http://0.0.0.0:8000`. ( or `http://localhost:8000`)

## Testing the Live Server

The live server is accessible at: `https://skinscanner.420777.xyz/predict`. This will be used to send requests directly to this endpoint for predictions when using the Skin Scanner App.

## Usage

To perform an inference, send a POST request to the `/predict` endpoint with an image file:
- **Endpoint:** `/predict`
- **Method:** `POST`
- **Form Data:** Image file with the key as `image`.

### Testing with Python

You can use Python's `requests` module to interact with the API. Run the `test_api.py`. 
Change the url to 'https://skinscanner.420777.xyz/predict' for the live server.

### Testing with cURL

```bash
curl -X POST -F "image=@path/to/your/image.jpg" https://skinscanner.420777.xyz/predict # or http://0.0.0.0:8000/predict for local
```

## Error Handling

The application returns error messages for the following scenarios:
- No image file provided: 400 status code with an error message.
- No file uploaded: 400 status code with an error message.
- Unexpected errors: 500 status code with a detailed error message.

## Docker Setup (Optional)

The repository includes a `Dockerfile` for containerization. You can build and run the application using Docker. However, this setup may need adjustments to suit your environment and can be ignored for initial testing. Refer to Docker documentation for building and running containers.
