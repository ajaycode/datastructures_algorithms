
class Node (object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList (object):
    def __init__ (self):
        self.head = None
        self.size = 0

    #)(1)
    def size_of_linked_list (self):
        return self.size

    #O(N)
    def size_after_iteration (self):
        start = self.head
        size = 0
        while (start is not None):
            size += 1
            start = start.next
        return (size)

    #O(1)
    def insert_at_start (self, data):
        self.size += 1
        new_node = Node (data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    #O(N) Linear Time Complexity
    def insert_at_end (self, data):
        self.size += 1
        new_node = Node (data)
        current_node = self.head
        while (current_node.next is not None):
            current_node = current_node.next
        current_node.next = new_node

    def remove (self, data):
        if self.head is None:
            return

        current_node = self.head
        previous_node = None
        node_to_be_removed = Node (data)
        while  (current_node is not None) and (current_node.data != data):
            previous_node  = current_node
            current_node = current_node.next

        if current_node is not None:
            self.size = self.size - 1
            if previous_node == None:
                self.head = current_node.next
            else:
                previous_node.next = current_node.next
            return True #element replaced
        else:
            return False #element not found


    #O(1)
    def get_first_element (self):
        first_element = self.head
        return first_element.data

    def get_all_elements (self):
        elements = []
        start = self.head
        while start is not None:
            elements.append(start.data)
            start = start.next
        return elements




if __name__ == '__main__':
    l1 = LinkedList ()
    l1.insert_at_start (5)

    element = l1.get_first_element()
    print (element)
    l1.insert_at_start(4)
    l1.insert_at_start(3)
    l1.insert_at_start(2)
    l1.insert_at_start(1)
    l1.insert_at_end(6)
    found = l1.remove (4)
    print ("Value is in list : {}".format(found))
    elements = l1.get_all_elements()
    for element in elements:
        print (element)
    print ("Size of Linked List = {}".format (l1.size_after_iteration()))
    print("Size of Linked List = {}".format(l1.size_of_linked_list()))