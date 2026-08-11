import json
class Car:
    def __init__(self, number, name, age, type, team, speed, capacity):
        self.set_number(number)
        self.set_name(name)
        self.set_age(age)
        self.set_type(type)
        self.set_team(team)
        self.set_speed(speed)
        self.set_capacity(capacity)
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
        if number <= 0:
            raise ValueError("Car number must be positive")
        self._number = number
    def set_name(self, name):
        if not name.strip():
            raise ValueError("Name cannot be empty")
        self._name = name
    def set_age(self, age):
        if age <= 0:
            raise ValueError("Age must be positive")
        self._age = age
    def set_type(self, type):
        if type not in ["Racer", "SupportVehicle"]:
            raise ValueError("Invalid vehicle type")
        self._type = type
    def set_team(self, team):
        if not team.strip():
            raise ValueError("Name cannot be empty")
        self._team = team
    def set_speed(self, speed):
        if speed <= 0:
            raise ValueError("Speed must be positive")
        self._speed = speed
    def set_capacity(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacity must be positive")
        self._capacity = capacity
    def calculate_performance(self):
        pass    
class Racer(Car):
    def __init__(self, number, name, age, type, team, speed, capacity, races, laps):
        super().__init__(number, name, age, type, team, speed, capacity)
        self.set_races(races)
        self.set_laps(laps)
    #racer getters and setters     
    def get_races(self):
        return self._races
    def get_laps(self):
        return self._laps
    def set_races(self, races):
        if races < 0:
            raise ValueError("Number of races cannot be negative")
        self._races = races
    def set_laps(self, laps):
        if laps < 0:
            raise ValueError("Number of laps cannot be negative")
        self._laps = laps 
    def calculate_performance(self):
        return (self.get_speed() * 10) + self.get_capacity()       
class SupportVehicle(Car):
    def __init__(self, number, name, age, type, team, speed, capacity, crewSize,reliability):
        super().__init__(number, name, age, type, team, speed, capacity)
        self.set_crewSize(crewSize)
        self.set_reliability(reliability)
    # getters    
    def get_crewSize(self):
        return self._crewSize
    def get_reliability(self):
        return self._reliability
    # Setters
    def set_crewSize(self, crewSize):
        if crewSize <= 0:
            raise ValueError("Crew size must be positive")
        self._crewSize = crewSize
    def set_reliability(self, reliability):
        if reliability < 0 or reliability > 10:
            raise ValueError("Reliability rating must be between 0 and 10")
        self._reliability = reliability
    def calculate_performance(self):
        return (self.get_speed() * 5) + (self.get_capacity() * 5)
#Menu validation functions      
def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.") 
def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Value must be positive.")
            else:
                return value
        except ValueError:
            print("Please enter a valid number.") 
def get_reliability(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0 or value > 10:
                print("Reliability must be between 0 and 10.")
            else:
                return value
        except ValueError:
            print("Please enter a valid number.")                          
def save_data():
    data = []
    for vehicle in garage:
        if vehicle.get_type() == "Racer":
            data.append({
                "number": vehicle.get_number(),
                "name": vehicle.get_name(),
                "age": vehicle.get_age(),
                "type": vehicle.get_type(),
                "team": vehicle.get_team(),
                "speed": vehicle.get_speed(),
                "capacity": vehicle.get_capacity(),
                "races": vehicle.get_races(),
                "laps": vehicle.get_laps()
            })
        else:
            data.append({
                "number": vehicle.get_number(),
                "name": vehicle.get_name(),
                "age": vehicle.get_age(),
                "type": vehicle.get_type(),
                "team": vehicle.get_team(),
                "speed": vehicle.get_speed(),
                "capacity": vehicle.get_capacity(),
                "crewSize": vehicle.get_crewSize(),
                "reliability": vehicle.get_reliability()
            })
    with open("garage.json", "w") as file:
        json.dump(data, file, indent=4)          
def load_data():
    global garage
    try:
        with open("garage.json", "r") as file:
            data = json.load(file)
            for item in data:
                if item["type"] == "Racer":
                    vehicle = Racer(
                        int(item["number"]),
                        item["name"],
                        item["age"],
                        item["type"],
                        item["team"],
                        item["speed"],
                        item["capacity"],
                        item["races"],
                        item["laps"]
                    )
                else:
                    vehicle = SupportVehicle(
                        int(item["number"]),
                        item["name"],
                        item["age"],
                        item["type"],
                        item["team"],
                        item["speed"],
                        item["capacity"],
                        item["crewSize"],
                        item["reliability"]
                    )
                garage.append(vehicle)
    except FileNotFoundError:
        pass

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
load_data()
option=None
while option!=7:
    print(Menu)
    option = get_integer("What's the move, Champ? ")
    if option < 1 or option > 7:
        print("Invalid option. Please choose a number from 1 to 7.")
        continue
    if option==1:
        number = get_positive_integer("Enter number: ")
        exist=False
        for car in garage:
            if car.get_number() == number:
                exist = True
                break 
        if exist:
            print("Car number already exists!")
            continue    
        name = input("Enter name: ")
        age = get_positive_integer("Enter age: ")
        print("""
        1. Racer
        2. Support Vehicle
        """)
        type_choice = get_integer("Choose vehicle type: ")
        if type_choice == 1:
            vtype = "Racer"
        elif type_choice == 2:
            vtype = "SupportVehicle"
        else:
            print("Invalid vehicle type.")
            continue
        team = input("Enter team: ")
        speed = get_positive_integer("Enter speed: ")
        capacity = get_positive_integer("Enter capacity: ")
        try:
            if vtype == "Racer":
                races=get_positive_integer("enter number of races completed: ")
                laps=get_positive_integer("enter number of laps completed: ")
                vehicle=Racer(number, name, age, "Racer", team, speed, capacity, races,laps)
            elif vtype == "SupportVehicle":
                crewSize=get_positive_integer("enter crew size: ")
                reliability=get_reliability("enter reliability rating: ")
                vehicle= SupportVehicle(number, name, age, "SupportVehicle", team, speed, capacity, crewSize,reliability)
            else:
                print("invalid vehicle type")
                continue
        except ValueError as e:
            print(e)
            continue    
        garage.append(vehicle)
        save_data()
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
    Performance Score: {vehicle.calculate_performance()}
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
    Performance Score: {vehicle.calculate_performance()}
    Crew Size: {vehicle.get_crewSize()}
    Reliability: {vehicle.get_reliability()}
    """)
                print("-" * 40) 
    elif option == 3:
        number = get_positive_integer("Enter vehicle number: ")
        found = False
        for vehicle in garage:
            if vehicle.get_number() == number:
                found = True
                print("""
    1. Name
    2. Team
    3. Speed
    4. Capacity
    5. Type-specific attribute
    """)
                choice = get_integer("What do you want to change? ")
                if choice == 1:
                    new_name = input("Enter new name: ")
                    vehicle.set_name(new_name)
                elif choice == 2:
                    new_team = input("Enter new team: ")
                    vehicle.set_team(new_team)
                elif choice == 3:
                    try:
                        new_speed = get_positive_integer("Enter new speed: ")
                        vehicle.set_speed(new_speed)
                    except ValueError as e:
                        print(e)
                elif choice == 4:
                    try:
                        new_capacity = get_positive_integer("Enter new capacity: ")
                        vehicle.set_capacity(new_capacity)
                    except ValueError as e:
                        print(e)
                elif choice == 5:
                    if vehicle.get_type() == "Racer":
                        print("""
    1. Races
    2. Laps
    """)
                        x = get_integer("Choose: ")
                        if x == 1:
                            new_races = get_positive_integer("Enter new races: ")
                            vehicle.set_races(new_races)
                        elif x == 2:
                            new_laps = get_positive_integer("Enter new laps: ")
                            vehicle.set_laps(new_laps)
                    elif vehicle.get_type() == "SupportVehicle":
                        print("""
    1. Crew Size
    2. Reliability
    """)
                        x =get_integer("Choose: ")
                        if x == 1:
                            new_crew = get_positive_integer("Enter new crew size: ")
                            vehicle.set_crewSize(new_crew)
                        elif x == 2:
                            new_reliability = get_reliability("Enter new reliability: ")
                            vehicle.set_reliability(new_reliability)
                print("Vehicle updated successfully!")
                save_data()
                break
        if not found:
            print("Vehicle not found!")
    elif option == 4:
        number = get_positive_integer("Enter vehicle number to retire: ")
        found = False
        for vehicle in garage:
            if vehicle.get_number() == number:
                confirmation = input(
                    "Are you sure you want to retire this vehicle? (y/n): "
                ).lower()
                while confirmation not in ["y", "n"]:
                    print("Please enter y or n.")
                    confirmation = input(
                        "Are you sure you want to retire this vehicle? (y/n): "
                    ).lower()
                if confirmation == "y":
                    garage.remove(vehicle)
                    save_data()
                    print("Vehicle retired successfully!")
                else:
                    print("Vehicle was not retired.")
                found = True
                break
        if not found:
            print("Vehicle not found!")
    elif option == 5:
        number = get_positive_integer("Enter vehicle number: ")
        found = False
        for vehicle in garage:
            if vehicle.get_number() == number:
                found = True
                if vehicle.get_type() == "Racer":
                    print(f"""
    Number: {vehicle.get_number()}
    Name: {vehicle.get_name()}
    Age: {vehicle.get_age()}
    Type: {vehicle.get_type()}
    Team: {vehicle.get_team()}
    Speed: {vehicle.get_speed()}
    Capacity: {vehicle.get_capacity()}
    Performance Score: {vehicle.calculate_performance()}
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
    Performance Score: {vehicle.calculate_performance()}
    Crew Size: {vehicle.get_crewSize()}
    Reliability: {vehicle.get_reliability()}
    """)
                break
        if not found:
            print("Vehicle not found!")    
    elif option == 6:
        if len(garage) == 0:
            print("Garage is empty.")
        else:
            total_cars = len(garage)
            total_performance = 0
            teams = {}
            for vehicle in garage:
                total_performance += vehicle.calculate_performance()
                team = vehicle.get_team()
                if team in teams:
                    teams[team] += 1
                else:
                    teams[team] = 1
            average_performance = total_performance / total_cars
            print(f"""
    ========== Garage Report ==========
    Total Cars Checked In: {total_cars}
    Average Performance Score: {average_performance:.2f}
    Cars Per Racing Team:
    """)
            for team in teams:
                print(f"{team}: {teams[team]}")
            print("==============================")                                               
else:
    print("goodbye")
   
              


