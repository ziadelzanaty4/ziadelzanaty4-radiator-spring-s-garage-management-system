class Car:
    def __init__(self, number, name, age, type, team, speed, capacity):
        self._number=number
        self._name=name
        self._age=age
        self._type=type
        self._team=team
        self._speed=speed
        self._capacity=capacity
    #getters    
    def get_number(self):
        return self._number
    def get_name(self):
        return self._name
    def get_age(self):
        return self._age
    def get_type(self):
        return self._type
    def get_team(self):
        return self._team
    def get_speed(self):
        return self._speed
    def get_capacity(self):
        return self._capacity 
    #setters   
    def set_number(self, number):
        self._number = number
    def set_name(self, name):
        self._name = name
    def set_age(self, age):
        self._age = age
    def set_type(self, type):
        self._type = type
    def set_team(self, team):
        self._team = team
    def set_speed(self, speed):
        self._speed = speed
    def set_capacity(self, capacity):
        self._capacity = capacity
class Racer(Car):
    def __init__(self, number, name, age, type, team, speed, capacity, races, laps):
        super().__init__(number, name, age, type, team, speed, capacity)
        self._races=races
        self._laps=laps
    #racer getters and setters     
    def get_races(self):
        return self._races
    def set_races(self, races):
        self._races = races
    def get_laps(self):
        return self._laps
    def set_laps(self, laps):
        self._laps = laps     
class SupportVehicle(Car):
    def __init__(self, number, name, age, type, team, speed, capacity, crewSize,reliability):
        super().__init__(number, name, age, type, team, speed, capacity)
        self._crewSize=crewSize
        self._reliability=reliability
    # getters    
    def get_crewSize(self):
        return self._crewSize
    def get_reliability(self):
        return self._reliability
    # Setters
    def set_crewSize(self, crewSize):
        self._crewSize = crewSize
    def set_reliability(self, reliability):
        self._reliability = reliability    


Menu= f"""
========Radiator Springs Garage========
1. Check in a car
2. View garage
3. Tune-up
4. Retire a car
5. Find a car
6. Garage report
7. Exit
=======================================
"""
garage = []
option=None
while option!=7:
    print(Menu)
    option=int(input("What's the move, Champ?"))
    if option==1:
        number = input("Enter number: ")
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        vtype = input("Enter type: ")
        team = input("Enter team: ")
        speed = float(input("Enter speed: "))
        capacity = int(input("Enter capacity: "))
        if vtype=="racer":
            races=int(input("enter number of races completed: "))
            laps=int(input("enter number of laps completed: "))
            vehicle=Racer(number, name, age, "Racer", team, speed, capacity, races,laps)
        elif vtype=="support":
            crewSize=int(input("enter crew size: "))
            reliability=float(input("enter reliability rating: "))
            vehicle= SupportVehicle(number, name, age, "SupportVehicle", team, speed, capacity, crewSize,reliability)
        else:
            print("invalid vehicle type")
            continue
        garage.append(vehicle)
        print("vehicle checked in successfully") 
    elif option == 2:
        if len(garage) == 0:
            print("Garage is empty.")
        else:
            for vehicle in garage:
                if vehicle.get_type() == "Racer":
                    print(f"""
    Number: {vehicle.get_number()}
    Name: {vehicle.get_name()}
    Age: {vehicle.get_age()}
    Type: {vehicle.get_type()}
    Team: {vehicle.get_team()}
    Speed: {vehicle.get_speed()}
    Capacity: {vehicle.get_capacity()}
    Races: {vehicle.get_races()}
    Laps: {vehicle.get_laps()}
    """)
                elif vehicle.get_type() == "SupportVehicle":
                    print(f"""
    Number: {vehicle.get_number()}
    Name: {vehicle.get_name()}
    Age: {vehicle.get_age()}
    Type: {vehicle.get_type()}
    Team: {vehicle.get_team()}
    Speed: {vehicle.get_speed()}
    Capacity: {vehicle.get_capacity()}
    Crew Size: {vehicle.get_crewSize()}
    Reliability: {vehicle.get_reliability()}
    """)
                print("-" * 40) 
                                         
   
              


