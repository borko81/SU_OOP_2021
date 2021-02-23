try:
    from one.cl_one import One
except:
    from cl_one import One


class Two:

    def __init__(self):
        One()
        print("Class Two")


if __name__ == '__main__':
    b = Two()
