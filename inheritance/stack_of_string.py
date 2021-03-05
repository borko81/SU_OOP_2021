class Stack:

    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.insert(0, item)

    def pop(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        return f"[{', '.join(self.data)}]"

if __name__ == '__main__':
    test = Stack()
    print(test.is_empty())
    test.push('1')
    test.push('2')
    print(test.is_empty())

    #import unittest


    # class StackTests(unittest.TestCase):
    #     def test_zero(self):
    #         stack = Stack()
    #         stack.push("apple")
    #         stack.push("carrot")
    #         self.assertEqual(str(stack), '[carrot, apple]')
    #         self.assertEqual(stack.pop(), 'carrot')
    #         self.assertEqual(stack.peek(), 'apple')
    #         stack.push("cucumber")
    #         self.assertEqual(str(stack), '[cucumber, apple]')
    #         self.assertEqual(stack.is_empty(), False)
    #
    #
    # if __name__ == '__main__':
    #     unittest.main()