from flask_app.config.mysqlconnection import connectToMySQL

from flask_app import DB, app

class Video:
    def __init__(self, data):
        self.id = data['id']
        self.filename = data['filename']
        self.notes = data['notes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO videos (filename, notes, created_at, updated_at, user_id) VALUE ( %(filename)s, %(notes)s, NOW(), NOW(), %(user_id)s );"
        return connectToMySQL(DB).query_db(query, data)
    

    @classmethod
    def get_all_by_user(cls, id):
        query = f"SELECT * FROM videos WHERE user_id = {id} ORDER BY id DESC"
        results = connectToMySQL(DB).query_db(query)
        videos = []
        for video in results:
            videos.append( cls(video) )
        return videos
    
