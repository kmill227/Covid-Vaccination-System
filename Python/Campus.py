from Alerts import Alerts
from DataBaseConnection import DataBase
import datetime
class Campus:
    def __init__(self, name):
        self.name = name
        self.alerts = Alerts()
        db = DataBase()
        sql = "SELECT * FROM campus WHERE CampusName=%s"
        arg = (self.name, )
        db.cursor.execute(sql, arg)
        campusData = db.cursor.fetchall()
        self.isRegional = campusData[0][1] 
        self.vaccineCount = campusData[0][2]
        self.vaccinesGiven = campusData[0][3]
        self.revenue = campusData[0][4]
        self.currentBrand = campusData[0][5]
        self.orderDate = campusData[0][6]
        db.connection.close()

        


    def lowVaccines(self):
        if self.vaccineCount == 0: 
            return 1
        return 0
        
    def orderVaccines(self):
        pass

    def computeRevenue(self):
        pass

    def getCurrentBrand(self):
        return self.currentBrand

    def bookVaccine(self):
        if self.currentBrand == "Johnson&Johnson":
            self.vaccineCount -= 1
            self.vaccinesGiven += 1
        else: 
            self.vaccineCount -= 2
            self.vaccinesGiven += 2

    def unBookVaccine(self):
        if self.currentBrand == "Johnson&Johnson":
            self.vaccineCount += 1
            self.vaccinesGiven -= 1
        else: 
            self.vaccineCount += 2
            self.vaccinesGiven -= 2


    def updateVaccineInfo(self):
        db = DataBase()
        sql = "UPDATE campus SET VaccinesOnHand = %s, VaccinesGiven = %s WHERE CampusName = %s"
        args = (self.vaccineCount, self.vaccinesGiven, self.name)
        db.cursor.execute(sql, args)
        db.connection.commit()
        db.connection.close()

    def receiveShipment(self):
        today = datetime.date.today()
        if self.orderDate == today:
            self.alerts.sendEmail(self.name)





    