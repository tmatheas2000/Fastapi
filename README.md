# FastAPI

This is a FastAPI application that allows users to perform CRUD operations on a database of products. The API provides endpoints for creating, reading, updating, and deleting products.

## Setup
### Setup Virtualenv:
      python3 -m virtualenv env
      cd env
      source bin/activate
      cd ..
    
### Install packages
    pip3 install -r requirements.txt

### Run Application
    uvicorn product.main:app --reload

### Generate SECRET_KEY
    openssl rand -hex 32

## Deployment Setup
- Install gcloud cli
- Install Docker
- Create a Google Cloud Project
- Enable Cloud Run API and Cloud Build API
- Link this Google Cloud Project with your Firebase project
- Create a Dockerfile with the config

## Deployment
### Authenticate with Google Cloud:
    gcloud auth login

### Set your Google Cloud project:
    gcloud config set project <your-project-id>

### Build the Docker container
    gcloud builds submit --tag gcr.io/<your-project-id>/fastapi-app

### Deploy the container to Cloud Run:
    gcloud run deploy fastapi-app \
      --image gcr.io/<your-project-id>/fastapi-app \
      --platform managed \
      --region <your-region> \
      --allow-unauthenticated