class Subject:

    def __init__(self):
        self._observer = []

    def notify(self, modifier=None):
        for observ in self._observer:
            if modifier != observ:
                observ.update(self)

    def attach(self, observer):
        if observer not in self._observer:
            self._observer.append(observer)

    def detach(self, observer):
        try:
            self._observer.remove(observer)
        except ValueError:
            pass


class Data(Subject):
    def __init__(self, name=''):
        super().__init__()
        self.name = name
        self._data = 0

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        self.notify()


class HexView:
    def update(self, subject):
        print(f"Hex {subject.name} - {subject.data}")


class DecimalViewer:
    """updates the Decimal viewer"""

    def update(self, subject):
        print('DecimalViewer: Subject % s has data % d' % (subject.name, subject.data))


if __name__ == "__main__":
    """provide the data"""

    obj1 = Data('Data 1')
    obj2 = Data('Data 2')

    view1 = DecimalViewer()
    view2 = HexView()

    obj1.attach(view1)