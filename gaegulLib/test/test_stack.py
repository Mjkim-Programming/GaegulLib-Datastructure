import unittest
from gaegulLib.stack import Stack

class TestStack(unittest.TestCase):
    def test_push_and_peek(self):
        s = Stack()
        self.assertTrue(s.is_empty())
        s.push(10)
        self.assertEqual(s.peek(), 10)
        s.push(20)
        self.assertEqual(s.peek(), 20)
        s.push(30)
        self.assertEqual(s.peek(), 30)

    def test_pop(self):
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertEqual(s.pop(), 3)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)
        self.assertTrue(s.is_empty())
        self.assertIsNone(s.pop())
        self.assertIsNone(s.peek())

    def test_mixed_operations(self):
        s = Stack()
        self.assertIsNone(s.pop())
        self.assertIsNone(s.peek())
        
        for i in range(5):
            s.push(i)
            self.assertEqual(s.peek(), i)
        
        self.assertEqual(s.pop(), 4)
        self.assertEqual(s.pop(), 3)
        self.assertEqual(s.peek(), 2)
        
        s.push(100)
        self.assertEqual(s.peek(), 100)
        
        self.assertEqual(s.pop(), 100)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)
        self.assertEqual(s.pop(), 0)
        self.assertTrue(s.is_empty())
        self.assertIsNone(s.pop())

if __name__ == "__main__":
    unittest.main()
