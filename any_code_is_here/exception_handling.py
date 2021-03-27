numbers = [1, 2, 3, 4, 5]


person = {
	"name": "Phil",
	"city": "Budapest"
}

try:
    print(numbers[100])
except LookupError as e:
    print(e)
except IndexError as e:
    print(e)


try:
    print(person[age])
except KeyError as e:
    print(e)