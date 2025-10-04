<!--
Release Process

This document outlines the steps required to build, test, and deploy Docker images for the application.
It includes instructions for local development, Docker Hub interaction, server login, and container management.
-->

# Release Process

### Step 1: Run the Docker Image
# Windows:
docker-compose up --build

# Mac:
docker compose up --build

### Step 2: Test the Local Build
Verify that the Docker image created in Step 1 is working correctly.
After testing, stop the container by pressing Ctrl+C.

### Step 3: Build the Docker Image
# Windows:
docker-compose build

# Mac:
docker compose build

### Step 4: Create a Docker Hub Repository
If a repository does not already exist on Docker Hub [https://hub.docker.com/], create a new PUBLIC repository.

### Step 5: Push the Docker Image to Docker Hub
1. Open System Terminal / Command Prompt.

2. List Docker images:
    docker images

3. Tag the Docker image:
    docker image tag IMAGE_ID DockerHubRepositoryName:RELEASE-0.1

    - Replace IMAGE_ID with the actual image ID.
    - Replace DockerHubRepositoryName with your Docker Hub repository name.
    - Ensure RELEASE is in uppercase and update the release number appropriately.?
    - Example:
        docker image tag 81a6b7374d4f ritesh2312/cogent-chatbot:RELEASE-0.1

4. Verify the image tagging:
    docker images

5. Push the image to Docker Hub:
    docker push DockerHubRepositoryName:TAG

    - Example:
        docker push ritesh2312/cogent-chatbot:RELEASE-0.1

    - Note: Only push the cogent-backend image, not the chromadb image. 

### Step 6: Login to the Server
1. Connect to Office VPN

2. Open Terminal and login to the server:
    ssh cogent@172.16.30.37

3. Enter the password when prompted.

### Step 7: Check Existing Docker Images [Always use sudo]
1. List running Docker containers:
    sudo docker ps

2. Stop the cogent-backend container:
    sudo docker stop CONTAINER_ID

3. Stop the chromadb container:
    sudo docker stop CONTAINER_ID

### Step 8: Pull and Run the Latest Docker Images
1. Pull the cogent-backend image:
    sudo docker pull ritesh2312/cogent-publish:RELEASE-0.1

2. Pull and run the chromadb image from Docker Hub based on the version used in the project (e.g., 0.5.5 which is currently used in project):
    sudo docker run -d --name chromadb --network cogentapp_network -p 8000:8000 chromadb/chroma:0.5.5

3. Run the updated cogent-backend image:
    sudo docker run -d --network cogentapp_network -p 5000:5000 ritesh2312/cogent-chatbot:RELEASE-0.1   

NOTE: For development server build images, change port 5000 to port 5001 and port 8000 to 8001 in above command and also in .env, dockerfile, start.sh and cogent_app.py files.   

### Step 9: Verify Docker Containers
1. List running Docker containers:
    sudo docker ps

    List all the containers:
    sudo docker ps -a 

### Step 10: Check Docker Image Logs
1. View all logs for a container:
    docker logs CONTAINER_ID

2. View the last 10 logs:
    docker logs -f --tail 10 CONTAINER_ID

3. View the last 100 logs:
    docker logs -f --tail 100 CONTAINER_ID