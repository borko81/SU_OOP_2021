def test_case01():
    assert 'name'.upper() == 'NAME'


class TestCase01:

    def test_case01(self):
        assert 'name'.upper() == 'NAME'

    def test_case02(self):
        assert 'name'.lower() == 'Name'