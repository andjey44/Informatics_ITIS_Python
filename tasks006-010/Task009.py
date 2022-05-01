class Car:
    coll_cars = 0

    def __init__(self, name):
        self.name = name
        Car.coll_cars += 1

    def get_name(self):
        return self.name

    def get_num_of_cars(self=None):
        return Car.coll_cars

    @staticmethod
    def another_stutic_metod():
        print('What is it?')


lamborgini = Car('lamborgini')
print(lamborgini.get_name())
print(lamborgini.get_num_of_cars())
print(lamborgini.get_num_of_cars())
Car.another_stutic_metod()