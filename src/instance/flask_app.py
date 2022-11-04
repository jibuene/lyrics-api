# instance/flask_app.py

# third-party imports
from flask import Flask
from flask_cors import CORS
from flask_restx import Api

# local imports
# from src.instance.config import config
# import src.misc.constants as cn
# from src.misc.service_logger import serviceLogger as logger

# flask application initialization
app = Flask(__name__)

# cross origin resource sharing
CORS(app)

# restplus swagger-ui
api = Api(app, version='1.0', title='lyrics-API', prefix='/api/v1',
          description='An API for lyrics services')

app.config['CORS_HEADERS'] = 'Content-Type'
