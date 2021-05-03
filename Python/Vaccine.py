class Vaccine:
    def __init__(self):
        self.brand = " "
        self.requiredDoses = 0

    def setCurrentBrand(self, brand):
        self.brand = brand
        self.setRequiredDoses()
    
    def setRequiredDoses(self):
        if self.brand == "Johnson&Johnson":
            self.requiredDoses = 1
        elif self.brand == "Moderna" or self.brand == "Pfizer":
            self.requiredDoses = 2

    def getRequiredDoses(self):
        return self.requiredDoses

    def getBrand(self):
        return self.brand
