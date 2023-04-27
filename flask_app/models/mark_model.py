from flask_app.config.mysqlconnection import connectToMySQL

from flask_app import DB, app

class Mark:
    def __init__(self, data):
        self.id = data['id']
        self.distance = data['distance']
        self.date = data['date']
        self.type = data['type']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO marks (distance, date, type, created_at, updated_at, user_id) VALUE ( %(distance)s, %(date)s, %(type)s, NOW(), NOW(), %(user_id)s );"
        return connectToMySQL(DB).query_db(query, data)
    
    @classmethod
    def get_all_by_user(cls, id):
        query = f"SELECT * FROM marks WHERE user_id = {id} ORDER BY id DESC"
        results = connectToMySQL(DB).query_db(query)
        marks = []
        for mark in results:
            marks.append( cls(mark) )
        return marks
