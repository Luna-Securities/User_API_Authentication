from flask import Blueprint, render_template, redirect, url_for, flash, jsonify, current_app
from flask_login import login_required, current_user
import requests
from .models import Todo
from . import auth

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return redirect(url_for('auth.login'))

@main.route('/api/users')
#Secure API endpoint with login_required decorator
@login_required
def api_users():
    user_name = current_user.name
    user_todos = Todo.query.filter_by(user_id=current_user.id).all()
    
    # Fetch user-specific API data
    api_data = get_user_api_data(current_user.id)
    
    if api_data is None:
        flash('Failed to fetch data from API.')
    
    return render_template('profile.html', name=user_name, user_todos=user_todos, api_data=api_data)

def get_user_api_data(user_id):
    # Fetch dummy data
    url = f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None