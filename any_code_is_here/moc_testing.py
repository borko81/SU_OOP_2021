from unittest.mock import Mock


m = Mock()
m.foo = 'bar'
m.configure_mock(bar='baz')

assert m.foo == 'bar'
assert m.bar == 'baz'

m.side_effect = ['foo', 'bar', 'baz']
assert m() == 'foo'
assert m() == 'bar'
assert m() == 'baz'
