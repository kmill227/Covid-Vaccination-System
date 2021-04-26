#include "Patient.h"

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