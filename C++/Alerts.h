#ifndef ALERTS_H
#define ALERTS_H
#include "VaccineOrder.h"

/************************
 * Class definition : Alerts
 * @author Kaleb Miller, Robert Silvey, Anthony Telerico, Carter Smith
 ************************/

class Alerts
{
    public: 
        void sendAlert(); 
        void websiteNotification(); 
    private: 
        VaccineOrder delivery; 
};

#endif