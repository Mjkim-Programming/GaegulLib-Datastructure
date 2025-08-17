import unittest
from gaegulLib.linked_list import LinkedList

class TestLinkedList(unittest.TestCase):
    def test_append_and_repr(self):
        lst = LinkedList()
        lst.append(1)
        lst.append(2)
        lst.appendleft(0)
        self.assertEqual(str(lst), "0<->1<->2")

    def test_pop(self):
        lst = LinkedList()
        lst.append(1)
        lst.append(2)
        self.assertEqual(lst.pop(), 2)
        self.assertEqual(str(lst), "1")

    def test_popleft(self):
        lst = LinkedList()
        lst.append(1)
        lst.append(2)
        self.assertEqual(lst.popleft(), 1)
        self.assertEqual(str(lst), "2")

    def test_pop_empty(self):
        lst = LinkedList()
        with self.assertRaises(IndexError):
            lst.pop()

    def test_popleft_empty(self):
        lst = LinkedList()
        with self.assertRaises(IndexError):
            lst.popleft()

if __name__ == "__main__":
    unittest.main()
