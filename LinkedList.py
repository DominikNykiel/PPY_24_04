class Element:
    def __init__(self, data=None, nextE=None):
        self.data = data
        self.nextE = nextE

    def __str__(self):
        return self.data


class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = None
        self.tail = None
        self.size = 0

    @staticmethod
    def defaultComparator(element1, element2):
        if element1.data >= element2.data:
            return 1
        elif element1.data < element2.data:
            return -1

        return 0

    def add_node(self, value):
        if self.head is None:
            self.tail = self.head = Element(value)
        else:
            self.tail.next = Element(value)
            self.tail = self.tail.next

        self.size += 1
        return self.tail


