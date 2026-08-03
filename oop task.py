class Car:
    def __init__(self, number, name, age, type, team, speed, capacity):
        self.number=number
        self.name=name
        self.age=age
        self.type=type
        self.team=team
        self.speed=speed
        self.capacity=capacity
class Racer(Car):
    def __init__(self, number, name, age, team, speed, capacity, races,laps):
        super().__init__(self, number, name, age, team, speed, capacity)
        self.races=races
        self.laps=laps  
class SupportVeichle(Car):
    def __init__(self, number, name, age, team, speed, capacity, CrewSize,ReliabilityRating):
        super().__init__(self, number, name, age, team, speed, capacity)
        self.CrewSize=CrewSize
        self.ReliabilityRating=ReliabilityRating              