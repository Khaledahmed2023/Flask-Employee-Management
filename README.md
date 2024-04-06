# Flask-Employee-Management

# Web Application README

## Overview
This web application is designed to provide functionality for user registration, user management, and user profile viewing. It includes features such as searching for users, sorting user lists, and viewing individual user profiles.

## Technologies Used
- Flask: Python web framework used for backend development.
- SQLAlchemy: Python SQL toolkit and Object-Relational Mapping (ORM) library used for database management.
- Flask-Migrate: Flask extension used for database migrations.
- Faker: Python library used for generating fake data.
- HTML/CSS: Frontend markup and styling languages.
- Jinja2: Templating engine for Python, used in combination with Flask for generating HTML content.

## Prerequisites
Before running the application, ensure you have the following dependencies installed:

- Python 3.x
- Flask
- Flask-Migrate
- SQLAlchemy

## Setup Instructions
1. Clone the repository to your local machine.
2. Install the required Python packages using pip:
    ```
    pip install -r requirements.txt
    ```
3. Configure the environment variables:
    - Set `DATABASE_URI_LOCAL` to your local database URI.
    - Set `SECRET_KEY` to a secure secret key for Flask session management.
    - Set `SECURITY_PASSWORD_SALT` to a secure salt for password hashing.
4. Create an `instance` folder in the root directory of the project.
5. Inside the `instance` folder, create a `config.py` file and define the following configurations:
    ```python
    # instance/config.py

    DATABASE_URI_LOCAL = 'sqlite:///your_database_name.db'
    SECRET_KEY = 'your_secret_key_here'
    SECURITY_PASSWORD_SALT = 'your_password_salt_here'
    ```
6. Run the Flask migrations to create and seed the database:
    ```
    flask db upgrade
    flask db-seed
    ```
7. Run the Flask application:
    ```
    python app.py
    ```
8. Access the application in your web browser at `http://localhost:5000`.

## File Structure
- **app.py**: Main Flask application file containing route definitions.
- **models.py**: SQLAlchemy models for database tables.
- **migration.py**: Alembic migration script for database schema changes.
- **templates/**: HTML templates for frontend views.
- **static/**: Static files (e.g., CSS, JavaScript) for frontend styling and behavior.
- **instance/**: Configuration folder containing environment-specific settings.

## Additional Notes
- The application includes basic styling using CSS. Feel free to modify the styles in `style.css` to match your design preferences.
- Faker is used to generate fake data for seeding the database. You can modify the `seed_data()` function in `models.py` to customize the generated data.
- Adjust the database URI in `instance/config.py` to connect to your preferred database management system.
