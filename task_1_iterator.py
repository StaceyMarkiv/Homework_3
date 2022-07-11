from itertools import cycle


class CyclicIterator:
    def __init__(self, container):
        self.container = container
        self.iterator = cycle(self.container)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iterator)


if __name__ == '__main__':
    testing1: list = [1, 2, 3, 4, 5, 6, 7]
    testing2: tuple = (1, 2, 3, 4, 5, 6, 7)
    testing3: set = {1, 2, 3, 4, 5, 6, 7}
    testing4: range = range(11)

    cyclic_iterator = CyclicIterator(testing4)
    for i in cyclic_iterator:
        print(i)
