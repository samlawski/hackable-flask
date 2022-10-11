import requests
from flask import Blueprint, render_template, request
from app.config import API_URL

blueprint = Blueprint('orders', __name__)

@blueprint.get('/checkout')
def get_checkout():
  return render_template('orders/index.html')

@blueprint.post('/checkout')
def post_checkout():
  try:
    if not all([
      request.form.get('message'),
      request.form.get('name'),
      request.form.get('street'),
      request.form.get('city'),
      request.form.get('zip'),
      request.form.get('card-number'),
      request.form.get('card-expire'),
      request.form.get('card-ccv'),
    ]):
      raise Exception('Please fill out all form fields.')

    requests.post(url=f'{API_URL}/api/checkout/', data=request.form)

    return render_template('orders/index.html',
      success='Purchase request successfully submitted'
    )
  except Exception as error_message:
    error = error_message or 'An error occurred while processing your order. Please make sure to enter valid data.'

    return render_template('orders/index.html',
      error=error
    )
    
