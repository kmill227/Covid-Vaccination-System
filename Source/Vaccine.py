class Vaccine:
    def __init__(self):
        self.brand = " "
        self.requiredDoses = 0

    def setCurrentBrand(self, brand):
        # set brand to given value
        self.brand = brand
        self.setRequiredDoses()
    
    def setRequiredDoses(self):
        #set required doses based on brand 
        if self.brand == "Johnson&Johnson":
            self.requiredDoses = 1
        elif self.brand == "Moderna" or self.brand == "Pfizer":
            self.requiredDoses = 2

    def getRequiredDoses(self):
        #return # of required doses based on brand
        return self.requiredDoses

    def getBrand(self):
        # return brand
        return self.brand
