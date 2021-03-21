# test first zero
import unittest
import time

from timeit import default_timer as timer


def exec_time(func):
    def wrapper(*args):
        t1 = timer()
        func(*args)
        end = timer()
        return end - t1

    return wrapper


class ExecTimeTests(unittest.TestCase):
    def test_zero_first(self):
        @exec_time
        def loop(start, end):
            total = 0
            for x in range(start, end):
                total += x
            return total

        self.assertEqual(round(loop(1, 10000000)), 1)


if __name__ == '__main__':
    unittest.main()
