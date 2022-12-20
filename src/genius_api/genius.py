from lyricsgenius import Genius
import os
from dotenv import load_dotenv

load_dotenv()

GENIUS_API_KEY = os.getenv('GENIUS_API_KEY')

class GeniusAPI:
  global genius
  genius = Genius(GENIUS_API_KEY)

  def searchByArtist(artist, max_songs):
    artist = genius.search_artist(artist, max_songs=max_songs, getRandom=True)
    if (artist == None or not hasattr(artist, 'songs') or len(artist.songs) == 0):
      return 'No results found'
    return artist.songs

  def searchByTag(tag, page):
    songs = []
    res = genius.tag(tag, page=page)
    for hit in res['hits']:
      songs.append(hit)
    return songs
