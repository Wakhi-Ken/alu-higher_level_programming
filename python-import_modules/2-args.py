#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    string = argv[1:]
    input_num = len(argv) - 1
    if input_num > 1:
        print("{} arguments:".format(input_num))
        for index in range(input_num):
            number = index + 1
            print("{}: {}".format(number, string[index]), end="\n")
    elif input_num == 1:
        print("1 argument:")
        number = 0
        print("{}: {}".format(input_num, string[number]), end="\n")
    else:
        print("0 arguments.")

