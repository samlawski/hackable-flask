import requests
from flask import Blueprint, render_template
from app.config import API_URL

blueprint = Blueprint('cookies', __name__)

@blueprint.get('/cookies')
def cookies():
  response = requests.get(url=f'{API_URL}/api/cookies/')
  cookies = response.json()

  return render_template('cookies/index.html', cookies=cookies)


@blueprint.get('/cookies/<id>')
def cookie(id):
  response = requests.get(url=f'{API_URL}/api/cookies/{id}')
  cookie = response.json()

  return render_template('cookies/show.html', cookie=cookie )

