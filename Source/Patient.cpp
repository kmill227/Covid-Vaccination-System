#include "Patient.h"
#include <fstream>
#include <cstdlib>
#include <iostream>
using namespace std; 

Insurance Patient::getInsurance()
{
    return insurancePolicy;
}

Appointment Patient::scheduledAppointment()
{
    return appts[0];
}

Vaccine Patient::vaccineInfo()
{
    return vaccination; 
}

bool Patient::vaccineCourseCompleted()
{
    return true; 
}

bool Patient::hasAppointment()
{
    return true; 
}

bool Patient::hasAccount()
{
    fstream vin; 
    vin.open("ValidLogins.csv");
    char validEmail[256], validPassword[256]; 

    if(vin.fail())
    {
        cout << "A fatal error has occurred";
        exit(1);
    }

    while(!vin.eof())
    {
        vin.get(validEmail, 255, ',');
        vin.get(validPassword, 255);
        if(strcmp(email, validEmail) == 0 && strcmp(password, validPassword) == 0)
        {
            return true; 
        }
        else
        {
            return false; 
        }
    }
    vin.close(); 
}

void Patient::LogIn()
{   
    cout << "Email: \n";
    cin >> email; 
    cout << "Password: \n";
    cin >> password; 

    if(hasAccount() == false)
    {
        char flag; 
        cout << "Incorrect login credentials, try again? (y/n)\n";
        cin >> flag; 
        if (flag == 'y' || flag == 'Y');
        {
            LogIn(); 
        }  
    }
}