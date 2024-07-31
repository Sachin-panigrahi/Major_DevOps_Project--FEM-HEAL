
# FEM-HEAL: Female Healthcare Management Web App

## Introduction

FEM-HEAL is a comprehensive healthcare management web application specifically designed to cater to female healthcare needs. This project aims to provide a seamless and user-friendly platform for managing various aspects of healthcare.
## Features

- **Common Disease Prediction**: Predict common diseases like flu, cold, headache, diarrhea, constipation, jaundice, dengue, typhoid, malaria, and more.
- **Ayurvedic Medicine Recommendations**: Get recommendations for ayurvedic treatments based on the predicted diseases.
- **User Authentication**: Secure login with username and password.

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Django
- **Containerization**: Docker
- **Orchestration**: Kubernetes
- **CI/CD**: Jenkins

## Project Structure

- **Django Application**: The core of the web app, handling the business logic and user interface.
- **Dockerfile**: Containerizes the application for consistency across different environments.
- **Kubernetes Manifests**: Manages the deployment, scaling, and operation of the app within a Kubernetes cluster.
- **Jenkins Pipeline**: Automates the deployment process from the GitHub repository to the Kubernetes cluster.

## Getting Started

### Prerequisites

- Docker
- Kubernetes
- Jenkins
- Git

### Installation

1. **Clone the repository:**
    git clone "https://github.com/Sachin-panigrahi/Major_DevOps_Project--FEM-HEAL.git"
    
2. **Build the Docker image:**
    docker build  .
    
3. **Deploy to Kubernetes:**
    kubectl apply -f Deployment.yaml
    kubectl apply -f Service.yaml
    
4. **Set up Jenkins:**
    - Create a Jenkins pipeline with the following stages:
        1. **Clone Repository**: Fetch the latest code from GitHub.
        2. **Build Docker Image**: Build the Docker image using the Dockerfile.
        3. **Push to Registry**: Push the Docker image to a Docker registry.
        4. **Deploy to Kubernetes**: Apply the Kubernetes manifests to deploy the application.

### Jenkins Pipeline

This Jenkins pipeline orchestrates the seamless deployment of the FEM-HEAL web application from our GitHub repository to a Kubernetes cluster. Here's a breakdown of the stages involved:

1. **Clone Repository**: Fetch the latest code from GitHub.
2. **Build Docker Image**: Build the Docker image using the Dockerfile.
3. **Push to Registry**: Push the Docker image to a Docker registry.
4. **Deploy to Kubernetes**: Apply the Kubernetes manifests to deploy the application.

## Usage

 **Access the Application**: Open your browser and navigate to the IP address or domain name of your Kubernetes cluster.


## Contributing

We welcome contributions from the community. If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`
3. Make your changes and commit them: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-branch`
5. Create a pull request.

By including all relevant details, this README file provides a clear overview of your FEM-HEAL project, instructions for setting up and using the application, and guidance on how to contribute.
