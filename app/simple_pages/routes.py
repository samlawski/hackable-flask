from flask import Blueprint, render_template

blueprint = Blueprint('simple_pages', __name__)

@blueprint.get('/')
def index():
  return render_template('simple_pages/index.html')
