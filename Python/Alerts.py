from DataBaseConnection import DataBase
class Alerts: 
    def __init__(self):
        self.send = False

    def lowVaccines(self, Campus):
        db = DataBase()
        db.cursor.execute("SELECT VaccinesOnHand FROM campus WHERE CampusName = '%s'", Campus)
        VaccineCount = db.cursor.fetchall()
        print(VaccineCount)

    def sendEmail(self):
        pass

    def displayOnMenu(self):
        pass


a = Alerts()
a.lowVaccines("Stark")