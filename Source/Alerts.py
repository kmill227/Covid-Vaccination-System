from DataBaseConnection import DataBase
import smtplib
import ssl

class Alerts: 
    def __init__(self):
        self.send = False
        self.addresses = []

    def sendEmail(self, campusName):
        # sends an email to every registered user in database
        port = 465
        password = "M4eyPrhKt3aRqQD"
        context = ssl.create_default_context()
        message = "The " + campusName + " Campus has just received a new shipment of Covid-19 vaccines."
        self.getAddresses()

        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login("cvisdemogroup1@gmail.com", password)
            for i in self.addresses:
                server.sendmail("cvisdemogroup1@gmail.com", i, message)
        
    def getAddresses(self): 
        #get email from login table of database
        db = DataBase()
        sql = "SELECT Email FROM logins"
        db.cursor.execute(sql)
        fetchedAddresses = db.cursor.fetchall()
        for i in fetchedAddresses:
            self.addresses.append(i[0]) 
        db.connection.close()


