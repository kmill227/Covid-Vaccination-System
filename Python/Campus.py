from Alerts import Alerts
from DataBaseConnection import DataBase
class Campus:
    def __init__(self):
        self.name = " "
        self.vaccineCount = 0
        self.isRegional = 1 
        self.revenue = 0
        self.alerts = Alerts()

    def lowVaccines(self):
        db = DataBase()
        sql = "SELECT VaccinesOnHand FROM campus WHERE CampusName=%s"
        arg = (self.name, )
        db.cursor.execute(sql, arg)
        self.vaccineCount = db.cursor.fetchone()
        sql = "SELECT isRegional FROM campus WHERE CampusName=%s"
        db.cursor.execute(sql, arg)
        self.isRegional = db.cursor.fetchone()
        if self.vaccineCount == 0: 
            alerts.sendEmail()
        if (self.vaccineCount < 50 and self.isRegional == 1) or (self.vaccineCount < 150 and self.isRegional == 0):
            self.orderVaccines()
        
        
    def orderVaccines(self):
        pass