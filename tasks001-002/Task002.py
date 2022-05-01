class Link:
    def __init__(self, value=None):
        self.value = value
        self.prev = self.next = None


class LinkedList:
    def __init__(self):
        self.head = Link()
        self.length = 0

    def get(self, n):
        now = self.head
        for i in range(n):
            now = now.next
        return now

    def insert(self, index, value):
        new = Link(value)
        new.next = self.get(index + 1)
        self.get(index).next = new
        self.length += 1

    def add(self, value):
        self.get(self.length).next = Link(value)
        self.length += 1

    def delete(self):
        element = self.get(self.length - 1).next
        self.get(self.length - 1).next = None
        self.length -= 1
        return element

    def count_value(self, value):
        now, k = self.head, 0
        for i in range(self.length):
            now = now.next
            k = k + 1 if now.value == value else 0
        return k

    def add_list(self, values):
        for value in values:
            self.add(value)

    def del_all(self):
        self.head.next = None
        self.length = 0

    def __len__(self):
        return self.length

    def __str__(self):
        our_s, s = self.head.next, ''
        for i in range(self.length):
            s += str(our_s.value) + ' '
            our_s = our_s.next
        return s


class LinkedStack(LinkedList):
    def __init__(self):
        super().__init__()


class LinkedQuery(LinkedList):
    def __init__(self):
        super().__init__()


class LinkedDeque(LinkedList):
    def __init__(self):
        super().__init__()


class LinkedSet(LinkedList):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    pass