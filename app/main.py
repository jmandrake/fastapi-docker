# Create virtual env: python -m venv venv
# Activate the virtual env: . venv/Scripts/activate

# Install fastapi in virtual env: pip install fastapi
# Install web server: pip install uvicorn

# Start the web server: uvicorn main:app --reload
# Create Dockerfile in root directory
# Compile the image: docker build -t python-fastapi .
# Run the new Docker image: docker run python-fastapi
# Mapping the docker port to the localhost port: docker run -p 8000:8000 python-fastapi
# Get all running containers: docker ps
# Get Docker container terminal: docker exec -it 1f66b7ec5af7 /bin/sh

# Docker Hub: docker login
# Upload image to Docker Hub: docker push username/image-name

### Upload to Github and use action to autobuild

from typing import Union
from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


if __name__=="__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")
