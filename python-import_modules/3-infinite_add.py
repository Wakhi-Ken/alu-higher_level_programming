#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    numbers = argv[1:]
    number = 0
    input_num = len(argv) - 1
    if input_num == 1:
        print("{}".format(numbers[0]), end="\n")
    elif input_num > 1:
        for index in range(input_num):
            number = number + int(numbers[index])
        print("{}".format(number), end="\n")
    elif input_num == 0:
        print(0)
