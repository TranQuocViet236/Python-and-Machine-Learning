from Abstractmethod import Car

Car_1 = Car("A", "B", "2021", "Blue")
Car_2 = Car("C", "D", "2022","Gray")
Car_1.Stop()
Car_1.Drive()
print(Car.wheels)
Car.wheels = 2
print(Car_1.wheels)
print(Car_2.wheels)

