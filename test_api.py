import requests

# URL of the Flask server
url = 'http://localhost:8000/predict' # 0.0.0.0 is the default address for all IPv4 addresses on the local machine

# Path to the sample image
image_path = 'C:\\Users\\soare\\Downloads\\0000.jpg'  # Update with your actual image path

# Send a POST request with the image file
with open(image_path, 'rb') as img_file:
    files = {'image': img_file}
    response = requests.post(url, files=files)

# Print the response from the server
print(response.json())