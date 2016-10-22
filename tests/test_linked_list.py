import sys
import unittest
from unittest import TestCase

sys.path.append('..\\')

from linked_list import *


class TestLinkedList (unittest.TestCase):

    def test_get_all_elements (self):
        l1 = LinkedList()
        l1.insert_at_start(5)
        l1.insert_at_start(4)
        l1.insert_at_start(3)
        l1.remove (5)
        l1.insert_at_end(6)
        self.assertEqual([3,4,6], l1.get_all_elements())
        self.assertEqual(l1.size_of_linked_list(), l1.size_after_iteration())


if __name__ == '__main__':
    unittest.main()



