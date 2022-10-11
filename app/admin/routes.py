import requests
from flask import Blueprint, render_template, request
from app.config import API_URL, ADMIN_PASSWORD, API_KEY

blueprint = Blueprint('admin', __name__)

@blueprint.get('/admin')
def admin():
  password = request.args.get('password')

  if password != ADMIN_PASSWORD:
    return 'You must provide an admin password to access this page.'

  response = requests.get(url=f'{API_URL}/api/users?key={API_KEY}')
  users = response.json()

  return render_template('admin/index.html', users=users)
