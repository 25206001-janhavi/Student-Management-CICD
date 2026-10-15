
# Student Management System

## Project Overview
This project demonstrates a CI/CD pipeline for a Python-based Student Management System using GitHub Actions and Docker.

## Technologies Used
- Python
- Flask
- Unit Testing
- Docker
- GitHub Actions

## Application
The Flask application provides student details in JSON format through the home endpoint.

## Testing
Unit tests verify that the application returns a successful response and the expected student data.

## Docker
Docker packages the application and its dependencies into a container.

## CI/CD Pipeline
GitHub Actions automatically builds the Docker image, runs unit tests, and checks whether the containerized application responds successfully.

## How to Run
1. Install the dependencies using `pip install -r requirements.txt`.
2. Run the tests using `python -m unittest -v`.
3. Start the application using `python app.py`.
4. Open `http://localhost:5000` in your browser.
