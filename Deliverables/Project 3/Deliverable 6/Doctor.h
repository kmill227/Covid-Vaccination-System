#ifndef DOCTOR_H
#define DOCTOR_H
#include <string>
#include "Station.h"

/************************
 * Class definition : Doctor
 * @author Kaleb Miller, Robert Silvey, Anthony Telerico, Carter Smith
 ************************/

class Doctor
{
    public: 
        int paySalary(); 
        void setStation(); 
        Station getStation(); 
        std::string getName();
        void printSchedule(); 
    private: 
        std::string name; 
        int salary; 
        Station workingStation; 
        Date workSchedule[30];
};
#endif