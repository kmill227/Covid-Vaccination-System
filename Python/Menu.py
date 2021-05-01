import tkinter as tk
from functools import partial
import User
import Admin
import Patient
import Alerts

class Menu:
    def __init__(self):
        self.currentUser = User.User()

    def LogInScreen(self):
        self.root = tk.Tk()
        self.root.geometry('300x150')
        self.root.title('CVIS Log-In')

        emailLabel = tk.Label(self.root, text="Email").grid(row=0, column=0)
        self.currentUser.email = tk.StringVar()
        emailEntry = tk.Entry(self.root, textvariable=self.currentUser.email).grid(row=0, column=1)

        passwordLabel = tk.Label(self.root, text="Password").grid(row=1, column=0)
        self.currentUser.password = tk.StringVar()
        passwordEntry = tk.Entry(self.root, textvariable=self.currentUser.password, show='*').grid(row=1, column=1)

        logIn = partial(self.currentUser.checkLogIn, self.root)

        loginButton = tk.Button(self.root, text="Login", command=logIn).grid(row=4, column=1)

        self.root.mainloop() 

        if self.currentUser.flag == 1:
            if self.currentUser.isAdmin == 1: 
                self.currentUser = Admin.Admin()
                adminMenu()
            else: 
                self.currentUser = Patient.Patient()
                patientMenu()
        elif self.currentUser.flag == 0: 
            self.root = tk.Tk()
            self.root.geometry('200x100')
            label = tk.Label(self.root, text="Invalid Login")
            accept = tk.Button(self.root, text ="OK", width = 20, command = lambda:[self.root.destroy(), self.LogInScreen()])
            label.pack()
            accept.pack()
            self.root.mainloop()

    def adminMenu(self):
        self.root = tk.Tk()
        self.root.geometry('400x100')
        button1 = tk.Button(self.root, text = "Register a new User", width = 50, command=self.currentUser.registerUser)
        button2 = tk.Button(self.root, text = "Display Booked Appointments", width = 50, command=self.currentUser.displayAllAppointments)
        button3 = tk.Button(self.root, text = "Log a Given Vaccine", width = 50, command=self.currentUser.logVaccine)
        button1.pack()
        button2.pack()
        button3.pack()
        self.root.mainloop()

    def patientMenu(self): 
        self.root = tk.Tk()
        self.root.geometry('400x100')
        button1 = tk.Button(self.root, text = "Create an appointment", width = 50, command=lambda:[self.root.destroy(), self.currentUser.appointments[self.currentUser.dosesCompleted].createAppointment()])
        button2 = tk.Button(self.root, text = "Cancel an Appointment", width = 50, command=lambda:[self.root.destroy(), self.currentUser.appointments[self.currentUser.dosesCompleted].cancelAppointment()])
        button3 = tk.Button(self.root, text = "Reschedule an Appointment", width = 50, command=lambda:[self.root.destroy(), self.currentUser.currentUser.appointments[self.currentUser.dosesCompleted].rescheduleAppointment()])
        button1.pack()
        button2.pack()
        button3.pack()
        self.root.mainloop()

        

    
menu = Menu()
menu.patientMenu()
