from src.instance.flask_app import api
from flask_restx import Resource, fields, reqparse
from src.misc.service_logger import serviceLogger as logger
from src.namespace import lyrics_api
from src.genius_api.genius import GeniusAPI
import json

def toJSON(self):
    return json.dumps(self, default=lambda o: o.__dict__, 
        sort_keys=True, indent=4)

@lyrics_api.route("/search/<string:artist>")
class search(Resource):
    def get(Resource, artist):
        """
        GET request endpoint of /search
        :return:

            [Song(id, artist, ...)]
        """
        song = GeniusAPI.searchByArtist(artist, 1)
        if (song == 'No results found' or len(song) == 0):
            return 'No result found', 404
        print(song)
        return song[0].to_text()
