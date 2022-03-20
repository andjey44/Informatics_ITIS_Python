class Flower:
    def __init__(self, names):
        self.names = names

    def __iter__(self):
        return iter(self.names)


class Lily:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


Lylies = [Lily('May'), Lily('Transcaucasian'), Lily('Pink'), Lily('Far Eastern')]
Flowers = Flower(Lylies)
for Flower in Flowers:
    print(Flower.get_name())