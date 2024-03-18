# User_API_Authentication
This is a simple Flask web application that demonstrates user authentication, API authentication, and integration with a third-party API (JSONPlaceholder) to pull data.

## Features

- **User Authentication:** Users can sign up, log in, and log out.
- **API Authentication:** The application uses Flask-Login to authenticate users for API access.
- **Third-Party API Integration:** It fetches data from the JSONPlaceholder API based on user authentication.

## Project Structure

Flask Project
|   README.txt
|   __init__.py
|   auth.py
|   main.py
|   models.py
|   templates/
|   |   base.html
|   |   login.html
|   |   signup.html
|   |   profile.html
|   venv/

- **auth.py:** Contains routes and logic for user authentication (sign up, log in, log out).
- **main.py:** Contains routes and logic for main application functionality, including API endpoints and third-party API integration.
- **models.py:** Defines database models (User, Todo).
- **templates/:** Directory containing HTML templates for rendering pages.
- **venv/:** Virtual environment directory.
- **__init__.py:** Initializes the Flask application.

## Usage

- **Sign Up:** Access /signup route to create a new user account.
- **Log In:** Access /login route to log in with your credentials.
- **Log Out:** Access /logout route to log out of your account.
- **Profile:** After logging in, you will be redirected to your profile page (/profile) where you can view user-specific data and interact with the application.

## Credits
- **Authors:** Janah Patricia Morano and Jan Christian Torres
