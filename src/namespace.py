# namespaces

from src.instance.flask_app import api

lyrics_api = api.namespace('lyrics', description='operations related to lyrics API')
