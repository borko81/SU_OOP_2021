def reverse_text(text):
    position = len(text) - 1
    while position >= 0:
        yield text[position]
        position -= 1


if __name__ == '__main__':
    for char in reverse_text("step"):
        print(char, end='')
