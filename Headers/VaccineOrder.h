#ifndef VACCINEORDER_H
#define VACCINEORDER_H
#include "Vaccine.h"
#include "Campus.h"
#include "Date.h"
#include "Station.h"
/************************
 * Class definition : VaccineOrder
 * @author Kaleb Miller, Robert Silvey, Anthony Telerico, Carter Smith
 ************************/

class VaccineOrder {

	public:

		bool canOrder(Campus campus);
		std::string getBrand();
		double getPrice();
		void order();

	private:
		
		std::string brand;
		Date deliverByDate;
		Station deliveryStation;
		double price;
		int orderAmount;
};
#endif
