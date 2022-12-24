[![Docker Image CI](https://github.com/jmandrake/fastapi-docker-template/actions/workflows/docker-image.yml/badge.svg)](https://github.com/jmandrake/fastapi-docker-template/actions/workflows/docker-image.yml)


# fastapi-docker
## Demo app using fastapi and docker

FastAPI Docker app with Github Actions autobuild

## Notes:
Create virtual env: python -m venv venv

Activate the virtual env: . venv/Scripts/activate

Install fastapi in virtual env: pip install fastapi

Install web server: pip install uvicorn

Start the web server: uvicorn main:app --reload

Create Dockerfile in root directory

Compile the image: docker build -t python-fastapi .

Run the new Docker image: docker run python-fastapi

Mapping the docker port to the localhost port: docker run -p 8000:8000 python-fastapi

Get all running containers: docker ps

Get Docker container terminal: docker exec -it 1f66b7ec5af7 /bin/sh

## Live demo:
Upload the docker tag (image) to hub.docker.com

Go to: https://labs.play-with-docker.com/

Import the image and launch it: 

docker pull username/docker-image-name

docker run username/docker-image-name

Or run it using port mapping:
docker run -p 8000:8000 username/docker-image-name
