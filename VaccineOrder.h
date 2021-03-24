#ifndef VACCINEORDER_H
#define VACCINEORDER_H

class VaccineOrder {

	public:

		bool canOrder()
		std::string getBrand()
		double getPrice()
		void order()

	private:
		
		std::string brand;
		Date deliverByDate;
		Station deliveryStation;
		double price;
		int orderAmount;
}

#endif
