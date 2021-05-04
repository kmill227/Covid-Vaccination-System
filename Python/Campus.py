from Alerts import Alerts
from DataBaseConnection import DataBase
import datetime
import random
import math

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
        self.orderNumber = campusData[0][6]
        self.orderDate = campusData[0][7]
        db.connection.close()

        


    def lowVaccines(self):
        if self.vaccineCount == 0: 
            return 1
        return 0
        
    def shouldOrder(self):
        if (self.vaccineCount < 50 and self.isRegional == 1) or (self.vaccineCount < 150 and self.isRegional == 0):
            return True
        else:
            return False
    
    def orderVaccines(self, requestNumber):
        fulfillNumber = ceil(requestNumber / 2)
        self.orderNumber = random.randint(fulfillNumber, requestNumber)
        day = random.randint(4,7)
        self.orderDate = datetime.date.today() + datetime.timedelta(days=day)
        db = DataBase()
        sql = "UPDATE campus SET NumberOrder = %s, deliveryDate = %s"
        args = (self.orderNumber, self.orderDate)
        db.cursor.execute()
        db.connection.commit()
        db.connection.quit()


    def computeRevenue(self):
        self.revenue = 0
        IDList = self.getUniqueUsersAtCampus()
        db = DataBase()
        InsuranceList = []
        for i in IDList:
            sql = "SELECT Insurance FROM users WHERE ID = %s"
            args = (i, )
            db.cursor.execute(sql, args)
            ins = db.cursor.fetchone()
            insuranceList.append(ins)
        for i in InsuranceList:
            if i == 1: 
                self.revenue += 120
            elif i == 0: 
                self.revenue -= 20 
        db.connection.close()
        self.updateRevenue()

    def updateRevenue(self):
        db = DataBase()
        sql = "UPDATE campus SET Revenue = %s WHERE CampusName = %s"
        args = (self.revenue, self.name)
        db.cursor.execute(sql, args)
        db.connection.commit()
        db.connection.close()

    def getCurrentBrand(self):
        return self.currentBrand

    def bookVaccine(self):
        if self.currentBrand == "Johnson&Johnson":
            self.vaccineCount -= 1
            self.vaccinesGiven += 1
        else: 
            self.vaccineCount -= 2
            self.vaccinesGiven += 1

    def unBookVaccine(self):
        if self.currentBrand == "Johnson&Johnson":
            self.vaccineCount += 1
            self.vaccinesGiven -= 1
        else: 
            self.vaccineCount += 2
            self.vaccinesGiven -= 1


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

    def getUniqueUsersAtCampus(self):
        db = DataBase()
        sql = "SELECT UserID FROM appointment WHERE Campus = %s"
        args = (self.name, )
        db.cursor.execute(sql, args)
        userIDList = db.cursor.fetchall()
        List1 = []
        List2 = []
        for i in userIDList:
            List1.append(i[0])

        db.connection.close()
        
        for i in List1:
            if i not in List2:
                List2.append(i)

        return List2







    