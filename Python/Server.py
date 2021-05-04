import Campus

campusNames = ["East Liverpool", "Geauga", "Kent", "Salem", "Stark", "Trumbull", "Tuscarawas"]
campusData = []

for i in campusNames:
    campusData.append(Campus.Campus(i))

for i in campusData: 
    if i.shouldOrder() == True: 
        if i.isRegional == 0:
            i.orderVaccines(150)
        elif i.isRegional == 1:
            i.orderVaccines(50)
    i.receiveShipment()