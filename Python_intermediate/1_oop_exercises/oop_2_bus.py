class Bus:
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
    def print_passengers(self):
        for passenger in self.passengers:
            print(passenger.name)

class Person:
    
    def __init__(self, name):
        self.name = name

school_bus = Bus()

miguel = Person("miguel")
luis = Person("luis")
nat = Person("nat")

# 3 con nombre + 10 numeradas = 13: el último no cabe
school_bus.add_passenger(miguel)
school_bus.add_passenger(luis)
school_bus.add_passenger(nat)

for number in range(4, 14):
    person = Person(str(number))
    school_bus.add_passenger(person)

print("--- Passengers on board ---")
school_bus.print_passengers()

school_bus.get_off_passenger(luis)

school_bus.get_off_passenger(Person("ana"))

print("--- After getting off ---")
school_bus.print_passengers()


