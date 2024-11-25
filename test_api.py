import requests

# URL of the Flask server
url = 'http://localhost:8000/predict' # or http://localhost:8000/predict if running locally

# Path to the sample image
image_path = 'path/to/your/image.jpg'  # Update with your actual image path

# Send a POST request with the image file
with open(image_path, 'rb') as img_file:
    files = {'image': img_file}
    response = requests.post(url, files=files)

# Print the response from the server
print(response.json())