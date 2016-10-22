import sys
import unittest
from unittest import TestCase

sys.path.append('..\\')

from stack import *


class TestStack (unittest.TestCase):

    def test_stack (self):
        s1 = Stack ()
        s1.push (10)
        s1.push (9)
        s1.push (8)
        s1.push (7)
        self.assertEqual(s1.pop(), 7)
        self.assertEqual(s1.peek(), 8)
        self.assertEqual(s1.pop(), 8)
        self.assertEqual(s1.pop(), 9)
        self.assertEqual(s1.stack_size(), 1)
        self.assertEqual(s1.pop(), 10)
        self.assertRaises(Exception, s1.pop)

        #self.assertEqual(s1.pop(), )


if __name__ == '__main__':
    unittest.main()