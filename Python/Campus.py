from Alerts import Alerts
from DataBaseConnection import DataBase
class Campus:
    def __init__(self, name):
        self.name = name
        self.alerts = Alerts()
        db = DataBase()
        sql = "SELECT * FROM campus WHERE CampusName=%s"
        arg = (self.name, )
        db.cursor.execute(sql, arg)
        campusData = db.cursor.fetchall()
        self.isRegional = campusData[1] 
        self.vaccineCount = campusData[2]
        self.vaccinesGiven = campusData[3]
        self.revenue = campusData[4]
        self.currentBrand = campusData[5]


    def lowVaccines(self):
        if self.vaccineCount == 0: 
            self.alerts.sendEmail()
        if (self.vaccineCount < 50 and self.isRegional == 1) or (self.vaccineCount < 150 and self.isRegional == 0):
            self.orderVaccines()
        
        
    def orderVaccines(self):
        pass