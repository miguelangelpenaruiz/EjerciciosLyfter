class Bus():
    max_passengers = 12

    def __init__(self):
        self.passengers = []

    def add_passenger(self,new_passenger):
        if len(self.passengers) >= self.max_passengers:
            print('The bus is full!!')
        else:
            self.passengers.append(new_passenger)

    def get_off_passenger(self, passenger):
        if passenger in self.passengers:
            self.passengers.remove(passenger)
        else:
            print("That passenger is not on the bus")

class Person():
    
    def __init__(self, name):
        self.name = name
        
miguel = Person("miguel")
luis = Person("luis")
nat = Person("nat")

a3_= Person("3")
a4_ = Person("4")
a5_ = Person("5")
a6_ = Person("6")
a7_ = Person("7")
a8_ = Person("8")
a9_ = Person("9")
a10_ = Person("10")
a11_ = Person("11")
a12_ = Person("12")

a13_ = Person("13")

school_bus = Bus()

school_bus.add_passenger(miguel)
school_bus.add_passenger(luis)

for passenger in school_bus.passengers:
    print(passenger.name)

school_bus.get_off_passenger(miguel)

for passenger in school_bus.passengers:
    print(passenger.name)

school_bus.get_off_passenger(nat)

school_bus.add_passenger(miguel)
school_bus.add_passenger(a3_)
school_bus.add_passenger(a4_)
school_bus.add_passenger(a5_)
school_bus.add_passenger(a6_)
school_bus.add_passenger(a7_)
school_bus.add_passenger(a8_)
school_bus.add_passenger(a9_)
school_bus.add_passenger(a10_)
school_bus.add_passenger(a11_)
school_bus.add_passenger(a12_)

school_bus.add_passenger(a13_)
