from Car import Car
from Motorbike import Motorbike
from Transport import Transport
from Truck import Truck

if __name__ == "__main__":
    c1 = Car("BMW", "777", 250, 1000)
    c2 = Car("Audi", "888", 240, 1200)
    m = Motorbike("Ducati", "111", 200, 111, True)
    t1 = Truck("Mercedes", "222", 150, 2100, True)
    t2 = Truck("Man", "333", 140, 2000, True)

    vehicles = [c1,c2,m,t1,t2]
    for vehicle in vehicles:
        vehicle.printData()

    Transport.CompareTo(vehicles)

    print("\n---------------------------------------Sorted---------------------------------------")

    for vehicle in vehicles:
        vehicle.printData()

    print("\n---------------------------------------Min requirement load capacity---------------------------------------")

    min_requirement = int(input("Введите минимальные требования к грузоподъемности: "))
    Transport.searchVehicleByLoadCapacity(vehicles, min_requirement)


