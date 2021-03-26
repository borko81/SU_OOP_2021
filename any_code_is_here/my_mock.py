from unittest.mock import Mock

mock = Mock(return_value=0)
for _ in range(5):
    print(mock())

mock = Mock(return_value=1)
print(mock())
mock = Mock(return_value=2)
print(mock.return_value)
print("=" * 20)
mock.side_effect = [1, 2, 3]
print(mock())
print(mock())
print(mock())
print("=" * 20)
mock = Mock()
print(mock(3, 4).call_args)