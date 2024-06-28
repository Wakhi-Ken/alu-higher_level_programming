#!/usr/bin/python3
def fizzbuzz():
    i = 1
    while i <= 100:
        fizz = i % 3
        buzz = i % 5
        if fizz == 0 and buzz == 0:
            print("{}".format("FizzBuzz"), end=" ")
        elif fizz == 0:
            print("{}".format("Fizz"), end=" ")
        elif buzz == 0:
            print("{}".format("Buzz"), end=" ")
        else:
            print("{}".format(i), end=" ")
        i += 1
fizzbuzz()

