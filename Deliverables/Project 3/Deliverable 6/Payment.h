#ifndef PAYMENT_H
#define PAYMENT_H

/************************
 * Class definition : Station
 * @author Kaleb Miller, Robert Silvey, Anthony Telerico, Carter Smith
 ************************/

class Payment
{
    public:
        void acceptPayment(); 
        bool isPaid(); 
    private: 
        int totalDue; 
};

#endif