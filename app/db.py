import sqlite3


class DBConnector:
    """
    Helper class for database connection / disconnection 
    """
    
    def __init__(self):
        self.conn = None

    def connect(self):
        self.conn = sqlite3.connect("/code/app.db")
        cursor = self.conn.cursor()
        return cursor
    
    def disconnect(self):
        self.conn.close()
