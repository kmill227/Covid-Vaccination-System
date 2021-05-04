from DataBaseConnection import DataBase
import datetime
import Menu 
import User
import Patient

user = Patient.Patient()
menu = Menu.LogInMenu(user)
menu.mainWindow()

if menu.successFlag == 1:
    pmenu = Menu.PatientMenu(user)
    pmenu.mainWindow()


















