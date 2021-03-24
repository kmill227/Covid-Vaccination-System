#ifndef PATIENT_H
#define PATIENT_H
#include "Appointment.h"
#include "Vaccine.h"
#include "Insurance.h"
class Patient
{
    public: 
        Insurance getInsurance(); 
        Appointment scheduledAppointment(); 
        Vaccine vaccineInfo(); 
        bool vaccineCourseCompleted(); 
    private:
};
#endif