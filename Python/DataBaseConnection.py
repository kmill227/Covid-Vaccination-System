import mysql.connector

class DataBase:

    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",   
            database="vaccination_system"
        )
        self.cursor = self.connection.cursor()










