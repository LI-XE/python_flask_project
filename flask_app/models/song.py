from flask_app.config.mysqlconnection import connectToMySQL

class Song:
  def __init__(self, data):
      self.id = data['id']
      self.title = data['title']
      self.artist = data['artist']
      self.rating = data['rating']
      self.created_at = data['created_at']
      self.updated_at = data['updated_at']

  @classmethod
  def get_all(cls):
      query = "SELECT * FROM songs;"
      results = connectToMySQL('lookify-office-hour').query_db(query)

      songs = []
      for song in results:
          songs.append(cls(song))

          return songs

  @classmethod
  def get_one(cls, id):
      query = "SELECT * FROM songs WHERE id= %(id)s"
      results = connectToMySQL(
          'lookify-office-hour').query_db(query, {'id': id})
      return results[0]


