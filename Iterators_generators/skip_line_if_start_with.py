from itertools import dropwhile

FILE = 'text.txt'

def read_file():
    with open(FILE, 'r') as f:
        for line in dropwhile(lambda x: x.startswith('#'), f):
            print(line)

