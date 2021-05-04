from DataBaseConnection import DataBase
import tkinter as tk

class User: 
    
    def __init__(self): 
        self.email = " "
        self.password = " "
        self.id = 0
        self.flag = 2
        self.isAdmin = 0
        self.name = ""



    def checkLogIn(self, email, password):
        self.email = email
        self.password = password
        db = DataBase()
        sql = "SELECT Email FROM logins"
        db.cursor.execute(sql)
        validEmails = db.cursor.fetchall() 
        found = False
        for i in validEmails:
            if i[0] == self.email:
                found = True
        if found == True:
            sql = "SELECT Password, ID, isAdmin FROM logins WHERE Email=%s"
            args = (self.email, )
            db.cursor.execute(sql, args)
            validPass = db.cursor.fetchone()
            if self.password != validPass[0]:
                self.flag = 0
            else: 
                self.id = validPass[1]
                self.isAdmin = validPass[2]
                self.flag = 1
        else: 
            self.flag = 0
        db.connection.close()

    def setName(self, name):
        self.name = name

    def getID(self):
        return self.id






