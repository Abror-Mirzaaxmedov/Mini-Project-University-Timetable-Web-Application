 Steps Followed During Development:

### 1. Setting up the EC2 Instance:
- Launched an AWS EC2 instance with Ubuntu.
- Connected to the EC2 instance using SSH.
- Ensured that the necessary ports (e.g., HTTP on port 80 and PostgreSQL on port 5432) were open in the security group.

###   2. Installing Python and Dependencies:  
- Installed Python 3 and the necessary dependencies (`python3-pip`) on the EC2 instance.
  - Ran `sudo apt update` and `sudo apt install python3 python3-pip -y`.
- If there were issues with `pip`, created a virtual environment (`python3 -m venv venv`) and activated it with `source venv/bin/activate`.

###   3. Setting up Amazon RDS for PostgreSQL:  
- Created an Amazon RDS PostgreSQL instance with the necessary configurations (username: `postgres`, password: `passwird`, endpoint: `postgres.c5wq22yyqd4d.eu-north-1.rds.amazonaws.com`).
- Set up the security group for the RDS instance to allow incoming connections on port 5432 from the EC2 instance.
- Created a PostgreSQL database on the RDS instance to store timetable data.

###   4. Setting up the Flask Application:  
- Created a new directory for the Flask application (`mkdir flask_app` and `cd flask_app`).
- Installed the required libraries: `Flask`, `psycopg2`, and `flask_sqlalchemy` using `pip`.
- Created the Flask app file (`app.py`) and wrote the following code to set up the application:

```python
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:passwird@postgres.c5wq22yyqd4d.eu-north-1.rds.amazonaws.com:5432/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Timetable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_level = db.Column(db.String(50), nullable=False)
    monday = db.Column(db.String(100))
    tuesday = db.Column(db.String(100))
    wednesday = db.Column(db.String(100))
    thursday = db.Column(db.String(100))
    friday = db.Column(db.String(100))

@app.route('/')
def home():
    timetable_data = Timetable.query.all()
    return render_template('index.html', timetable=timetable_data)

if __name__ == "__main__":
    app.run(debug=True)
```

- The `Timetable` model was created in SQLAlchemy to store timetable data in the database.

###   5. Setting Up Templates:  
- Created an HTML file (`templates/index.html`) to display the timetable dynamically.
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Timetable</title>
</head>
<body>
    <h1>Student Timetable</h1>
    <table border="1">
        <thead>
            <tr>
                <th>Student Level</th>
                <th>Monday</th>
                <th>Tuesday</th>
                <th>Wednesday</th>
                <th>Thursday</th>
                <th>Friday</th>
            </tr>
        </thead>
        <tbody>
            {% for entry in timetable %}
                <tr>
                    <td>{{ entry.student_level }}</td>
                    <td>{{ entry.monday }}</td>
                    <td>{{ entry.tuesday }}</td>
                    <td>{{ entry.wednesday }}</td>
                    <td>{{ entry.thursday }}</td>
                    <td>{{ entry.friday }}</td>
                </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>
```

###   6. Dockerizing the Flask Application:  
- Created a `Dockerfile` to package the Flask application into a Docker container:

```Dockerfile
# Use official Python image as a base
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application files into the container
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py"]
```

- Created a `requirements.txt` file containing the required Python packages:
```
Flask
psycopg2
flask_sqlalchemy
```

- Built and ran the Docker container:
  - `docker build -t flask_app .`
  - `docker run -p 5000:5000 flask_app`

###   7. Running the Flask Application:  
- The Flask application is now accessible at `http://<EC2-public-IP>:5000`.

###   8. Accessing the Database:  
- Used DBeaver to connect to the PostgreSQL database hosted on RDS by providing the database URI in the format:
  ```
  jdbc:postgresql://postgres.c5wq22yyqd4d.eu-north-1.rds.amazonaws.com:5432/mydb
  ```
  - Entered the RDS username (`postgres`) and password (`passwird`) to establish the connection.

###   9. Debugging and Final Adjustments:  
- Ensured the connection to the database worked by testing it in the Flask app.
- Corrected any issues with the RDS endpoint, username, password, and firewall settings.
- Finalized the application code and Docker setup.

---

##   Source Code for the Flask Application:  

  `app.py`  :

```python
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:passwird@postgres.c5wq22yyqd4d.eu-north-1.rds.amazonaws.com:5432/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Timetable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_level = db.Column(db.String(50), nullable=False)
    monday = db.Column(db.String(100))
    tuesday = db.Column(db.String(100))
    wednesday = db.Column(db.String(100))
    thursday = db.Column(db.String(100))
    friday = db.Column(db.String(100))

@app.route('/')
def home():
    timetable_data = Timetable.query.all()
    return render_template('index.html', timetable=timetable_data)

if __name__ == "__main__":
    app.run(debug=True)
```

  `templates/index.html`  :

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Timetable</title>
</head>
<body>
    <h1>Student Timetable</h1>
    <table border="1">
        <thead>
            <tr>
                <th>Student Level</th>
                <th>Monday</th>
                <th>Tuesday</th>
                <th>Wednesday</th>
                <th>Thursday</th>
                <th>Friday</th>
            </tr>
        </thead>
        <tbody>
            {% for entry in timetable %}
                <tr>
                    <td>{{ entry.student_level }}</td>
                    <td>{{ entry.monday }}</td>
                    <td>{{ entry.tuesday }}</td>
                    <td>{{ entry.wednesday }}</td>
                    <td>{{ entry.thursday }}</td>
                    <td>{{ entry.friday }}</td>
                </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>
```

  `Dockerfile`  :

```Dockerfile
# Use official Python image as a base
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application files into the container
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py"]


