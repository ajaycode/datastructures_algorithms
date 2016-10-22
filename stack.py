from linked_list import *

class Stack (object):
    def __init__(self):
        self.linked_list = LinkedList ()

    def stack_size (self):
        return self.linked_list.size_of_linked_list()

    def is_empty (self):
        return self.linked_list.size_of_linked_list() == 0

    def push (self, data):
        self.linked_list.insert_at_start(data)

    def pop (self):
        if not self.is_empty():
            data = self.linked_list.get_first_element()
            self.linked_list.remove(data)
            return  data
        else:
            raise Exception("No more entries in stack.")

    def peek (self):
        if not self.is_empty():
            return self.linked_list.get_first_element()


if __name__ == '__main__':
    s1 = Stack ()
    s1.push (10)
    s1.push (9)
    s1.push (8)
    print (s1.peek())
    while not s1.is_empty():
        print (s1.pop())


