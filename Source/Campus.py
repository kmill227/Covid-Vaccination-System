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
        self.orderPlaced = campusData[0][8]
        db.connection.close()

        


    def lowVaccines(self):
        # return 1 if out of vaccines, else return 0 
        if self.vaccineCount == 0: 
            return 1
        return 0
        
    def shouldOrder(self):
        #returns True if regional campus has less than 50 vaccines, or kent has less than 150, else returns false
        if (self.vaccineCount < 50 and self.isRegional == 1) or (self.vaccineCount < 150 and self.isRegional == 0) and self.orderPlaced == 0:
            return True
        else:
            return False
    
    def orderVaccines(self, requestNumber):
        # place a vaccine order and log it to the database using random number generator to simulate pharmaceutical company
        fulfillNumber = math.ceil(requestNumber / 2)
        self.orderNumber = random.randint(fulfillNumber, requestNumber)
        day = random.randint(4,7)
        self.orderDate = datetime.date.today() + datetime.timedelta(days=day)
        self.orderPlaced = 1
        db = DataBase()
        sql = "UPDATE campus SET NumberOrder = %s, deliveryDate = %s, OrderPlaced = %s  WHERE campusName = %s"
        args = (self.orderNumber, self.orderDate, self.orderPlaced, self.name)
        db.cursor.execute(sql, args)
        db.connection.commit()
        db.connection.close()


    def computeRevenue(self):
        # calculates revenue, +120 for every insured patient at campus, -20 for uninsured and
        self.revenue = 0
        IDList = self.getUniqueUsersAtCampus()
        db = DataBase()
        insuranceList = []
        for i in IDList:
            sql = "SELECT Insurance FROM users WHERE ID = %s"
            args = (i, )
            db.cursor.execute(sql, args)
            ins = db.cursor.fetchone()[0]
            insuranceList.append(ins)
        for i in insuranceList:
            if i == 1: 
                self.revenue += 120
            elif i == 0: 
                self.revenue -= 20 
        self.updateRevenue()
        db.connection.close()

    def updateRevenue(self):
        #logs revenue to database
        db = DataBase()
        sql = "UPDATE campus SET Revenue = %s WHERE CampusName = %s"
        args = (self.revenue, self.name)
        db.cursor.execute(sql, args)
        db.connection.commit()
        db.connection.close()

    def getCurrentBrand(self):
        #return brand used at campus
        return self.currentBrand

    def bookVaccine(self):
        #decrease #of vaccines at campus by 1 if J&J, by 2 if other, increase # of vaccinations by 1  
        if self.currentBrand == "Johnson&Johnson":
            self.vaccineCount -= 1
            self.vaccinesGiven += 1
        else: 
            self.vaccineCount -= 2
            self.vaccinesGiven += 1

    def unBookVaccine(self):
        # Increase # of vaccines at campus by 1 if J&J, 2 otherwise 
        if self.currentBrand == "Johnson&Johnson":
            self.vaccineCount += 1
            self.vaccinesGiven -= 1
        else: 
            self.vaccineCount += 2
            self.vaccinesGiven -= 1


    def updateVaccineInfo(self):
        # log updated vaccine info to db
        db = DataBase()
        sql = "UPDATE campus SET VaccinesOnHand = %s, VaccinesGiven = %s WHERE CampusName = %s"
        args = (self.vaccineCount, self.vaccinesGiven, self.name)
        db.cursor.execute(sql, args)
        db.connection.commit()
        db.connection.close()

    def receiveShipment(self):
        # check if current date = order receiving date, log to database
        today = datetime.date.today()
        if self.orderDate == today:
            self.orderPlaced = 0
            self.alerts.sendEmail(self.name)

        db = DataBase()
        sql = "UPDATE campus SET OrderPlaced = %s WHERE campusName = %s"
        args = (self.orderPlaced, self.name)
        db.cursor.execute(sql, args)
        db.connection.commit()
        db.connection.close()

    def getUniqueUsersAtCampus(self):
        # get all unique users with appointment at campus, returns a list of all unique user IDs
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







    