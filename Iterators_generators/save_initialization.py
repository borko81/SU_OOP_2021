"""
Read file, if search word in line, show histlen line and line with match
"""


from collections import deque

FILE = 'text.txt'


class linexist:

    def __init__(self, lines, histlen=2):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line


with open(FILE, 'r') as f:
    lines = linexist(f)
    for line in lines:
        if 'borko' in line:
            for lineno, hline in lines.history:
                print(lineno, hline.strip())
