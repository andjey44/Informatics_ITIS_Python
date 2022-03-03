import abc


class Car(abc.ABC):
    def __init__(self, speed):
        self.max_speed = speed
        self.comfort_speed = speed//4

    @abc.abstractmethod
    def show(self):
        pass

    def is_even_max_speed(self):
        return not(self.max_speed % 2)

    def is_even_comfort_speed(self):
        return not(self.comfort_speed % 2)

    def nyzno_snizit(self):
        return self.max_speed - self.comfort_speed


class Motobyke(Car):
    def __init__(self, speed):
        super().__init__(speed)
        self.min_speed = self._min_speed()
        if self.min_speed is not None:
            raise ValueError("Your car is break")

    def show(self):
        print(f'Speed: {self.max_speed}, Min_speed in sequence: {self.min_speed}')

    def _min_speed(self):
        if self.comfort_speed*4 == self.max_speed:
            return 0
        else:
            return -1

    def nyzno_snizit(self):
        return self.max_speed - self.comfort_speed

class Bicycle(Car):
    def __init__(self, speed):
        super().__init__(speed)
        self.sred_speed = self._sred_speed()
        if self.sred_speed is None:
            raise ValueError("Your car is break")

    def _min_speed(self):
        if self.comfort_speed * 4 == self.max_speed:
            return 0
        else:
            return -1

    def show(self):
        print(f'Speed: {self.max_speed}, Sred_speed in sequence: {self.sred_speed}')

    def _sred_speed(self):
        if self._min_speed() >= 0:
            return (self.max_speed+self._min_speed)//2
        else:
            return 0

    def nyzno_snizit(self):
        return self.max_speed - self.comfort_speed


class Multi_Byke(Motobyke, Bicycle):
    def __init__(self, number):
        super().__init__(number)
