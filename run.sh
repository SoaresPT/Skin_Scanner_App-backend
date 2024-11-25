#!/bin/bash

# Navigate to the script directory to handle relative paths correctly
cd "$(dirname "$0")"

# Variables
CONTAINER_NAME="skinscanner"
IMAGE_NAME="skinscanner"
NETWORK_NAME="zipline_default"  # Use your identified network name
PORT_MAPPING="8000:8000"

# Stop and remove the existing container if it exists
if [ "$(docker ps -q -f name=$CONTAINER_NAME)" ]; then
    echo "Stopping and removing existing container..."
    docker stop $CONTAINER_NAME
    docker rm $CONTAINER_NAME
else
    echo "No existing container found. Moving on..."
fi

# Build the Docker image
echo "Building the Docker image..."
docker build -t $IMAGE_NAME .

# Run the container with restart policy unless-stopped
echo "Running the Docker container..."
docker run -d \
    --name $CONTAINER_NAME \
    --network $NETWORK_NAME \
    --restart unless-stopped \
    -p $PORT_MAPPING \
    $IMAGE_NAME

echo "Container is now up and running..."