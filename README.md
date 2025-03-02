# Flask Ignite

A simple Flask app creator that automatically generates a basic Flask project structure including models, routes, services, configuration, and more.

## Getting Started

This repository contains a utility package that, once installed, provides a CLI command to create a Flask project structure automatically. The command is registered as a console script named `flask-admin`.

## Prerequisites

- Python 3.7 or higher
- [Flask](https://flask.palletsprojects.com/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)
- [Flask-Migrate](https://flask-migrate.readthedocs.io/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

## Setup and Usage

1. **Clone the Repository**

   Clone this repository to your local machine.

2. **Install the Package**

   From the root of the repository, install the package locally:

   ```sh
   pip install flask-ignite
   ```

3. **Run the Project Setup Command**

   Execute the following command to generate the Flask project structure:

   ```sh
   flask-ignite --project <your_project_name> # defaults to flask_app
   ```

   This will create a project structure similar to the following:

   - **flask_app/**
     - **app/**
       - **models/**
         - `__init__.py`
         - `user.py`
         - `post.py`
       - **routes/**
         - `__init__.py`
         - `user_routes.py`
         - `post_routes.py`
       - **services/**
         - `__init__.py`
         - `user_service.py`
       - **config/**
         - `__init__.py`
         - `settings.py`
       - `extensions.py`
       - `__init__.py`
     - **migrations/**
     - `.env`
     - `config.py`
     - `requirements.txt`
     - `wsgi.py`
     - `run.py`

4. **Next Steps**

   After generating the project, follow these steps:

   - Navigate into the generated project directory:

     ```sh
     cd flask_app
     ```

   - Create a virtual environment:

     ```sh
     python -m venv venv
     ```

   - Activate the virtual environment:

     - **Windows:**
       ```sh
       venv\Scripts\activate
       ```
     - **Mac/Linux:**
       ```sh
       source venv/bin/activate
       ```

   - Install the project dependencies:

     ```sh
     pip install -r requirements.txt
     ```

   - Initialize the database:

     ```sh
     flask db init && flask db migrate -m "Initial migration" && flask db upgrade
     ```

   - Run the app:

     ```sh
     python run.py
     ```

## Project Structure Overview

- **app/models**: Contains database models (e.g., `User` and `Post` defined in `user.py` and `post.py`).
- **app/routes**: Defines routes using Blueprints for handling API endpoints (in `user_routes.py` and `post_routes.py`).
- **app/services**: Holds service functions for data manipulation or retrieval (in `user_service.py`).
- **app/config**: Stores configuration settings and environment-specific variables (in `settings.py`).
- **app/extensions.py**: Initializes Flask extensions like SQLAlchemy and Migrate.
- **app/**init**.py**: Creates and configures the Flask application.

## License

This project is licensed under the MIT License.

## Author

Nahom D  
Email: nahom@nahom.eu.org
