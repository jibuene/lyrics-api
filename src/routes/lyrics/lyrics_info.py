from src.instance.flask_app import api
from flask_restx import Resource, fields, reqparse
from src.misc.service_logger import serviceLogger as logger
from src.namespace import lyrics_api
from src.genius_api.genius import GeniusAPI

@lyrics_api.route("/search/<string:artist>")
class search(Resource):
    def get(Resource, artist):
        """
        GET request endpoint of /search
        :return:

            [Song(id, artist, ...)]
        """
        xd = GeniusAPI.searchByArtist(artist, 1)[0]
        print(xd.lyrics)
        return xd.lyrics
