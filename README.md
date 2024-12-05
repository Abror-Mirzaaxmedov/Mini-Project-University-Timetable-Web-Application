# Mini-Project-University-Timetable-Web-Application

Project Description:
This project is a Flask web application that dynamically displays a timetable for students based on their levels. The application is hosted on an EC2 instance and connects to a PostgreSQL database hosted on Amazon RDS.

Steps to Set Up:
EC2 Setup:
Launch an EC2 instance and set up security groups.

RDS Setup:
Create an Amazon RDS instance for PostgreSQL and configure security groups.

Flask Application:
Set up a Flask app that connects to the PostgreSQL database.

Docker Setup:
Dockerize the Flask application using a Dockerfile and deploy the app.

Running the Application:
Set up the EC2 instance.
Create the PostgreSQL database in RDS.
Clone or download the Flask app.

Install necessary packages and dependencies.

Run the Flask application:
python app.py or via Docker:
docker run -p 5000:5000 flask_app
