class Car:
    def __init__(self, number, name, age, type, team, speed, capacity):
        self._number=number
        self._name=name
        self._age=age
        self._type=type
        self._team=team
        self._speed=speed
        self._capacity=capacity

class Racer(Car):
    def __init__(self, number, name, age, team, speed, capacity, races,laps):
        super().__init__(self, number, name, age, team, speed, capacity)
        self._races=races
        self._laps=laps  
class SupportVeichle(Car):
    def __init__(self, number, name, age, team, speed, capacity, CrewSize,ReliabilityRating):
        super().__init__(self, number, name, age, team, speed, capacity)
        self._CrewSize=CrewSize
        self._ReliabilityRating=ReliabilityRating



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
option=None
while option!=7:
    print(Menu)
    option=int(input("What's the move, Champ?"))

