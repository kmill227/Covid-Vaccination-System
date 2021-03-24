#ifndef VACCINE_H
#define VACCINE_H

#include <string>
#include "Date.h"

/************************
 * Class definition : Vaccine
 * @author Kaleb Miller, Robert Silvey, Anthony Telerico, Carter Smith
 ************************/

class Vaccine {

	public:

		std::string getBrand();
		double getPrice();
		int getId();
		Date getDate();
		int getDoseNumber();

	private:
		std::string Brand;
		double price;
		int id;
		int date;
		int doseNumber;
};

#endif
