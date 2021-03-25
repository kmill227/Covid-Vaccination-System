#ifndef STATION_H
#define STATION_H
#include "Campus.h"
#include "VaccineOrder.h"
/************************
 * Class definition : Station
 * @author Kaleb Miller, Robert Silvey, Anthony Telerico, Carter Smith
 ************************/

class Station
{
    public: 
        VaccineOrder placeOrder(); 
    private: 
        int vaccinesOnHand;
        Campus location;
};

#endif