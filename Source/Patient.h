#ifndef PATIENT_H
#define PATIENT_H
#include "Appointment.h"
#include "Vaccine.h"
#include "Insurance.h"

/************************
 * Class definition : Patient
 * @author Kaleb Miller, Robert Silvey, Anthony Telerico, Carter Smith
 ************************/

class Patient
{
    public: 
        Insurance getInsurance(); 
        Appointment scheduledAppointment(); 
        Vaccine vaccineInfo(); 
        bool vaccineCourseCompleted(); 
        bool hasAppointment();
        bool hasAccount(); 
        void LogIn(); 
    private:
        int idNumber;
        char name[256];
        char email[256]; 
        char password[256]; 
        Vaccine vaccination; 
        Appointment appts[2]; 
        Insurance insurancePolicy; 
};
#endif