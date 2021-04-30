from DataBaseConnection import DataBase
class Alerts: 
    def __init__(self):
        self.send = False

    def lowVaccines(self, Campus):
        db = DataBase()
        sql = "SELECT VaccinesOnHand FROM campus WHERE CampusName=%s"
        arg = (Campus, )
        db.cursor.execute(sql, arg)
        vaccineCount = db.cursor.fetchone()
        if vaccineCount == 0: 
            self.sendEmail()
        
        

    def sendEmail(self):
        pass

    def displayOnMenu(self):
        pass


a = Alerts()
a.lowVaccines("Stark")