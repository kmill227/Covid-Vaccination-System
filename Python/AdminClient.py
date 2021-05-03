from DataBaseConnection import DataBase

flag = 0
db = DataBase()
sql = "SELECT ID FROM users"
db.cursor.execute(sql)
validIds = db.cursor.fetchall()
db.connection.close()
for i in validIds:
    print(i)