from flask import Flask
from . import cookies, simple_pages, orders, admin

def create_app():
  app = Flask(__name__)
  app.config.from_object('app.config')

  register_extensions(app)
  register_blueprints(app)

  return app

# Blueprints
def register_blueprints(app: Flask):
  app.register_blueprint(cookies.routes.blueprint)
  app.register_blueprint(simple_pages.routes.blueprint)
  app.register_blueprint(orders.routes.blueprint)
  app.register_blueprint(admin.routes.blueprint)

  return True

# Extensions
def register_extensions(app: Flask):
  # db.init_app(app)
  return True