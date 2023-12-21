# Write a program that prints the numbers from 1 to 100.
# But for multiples of three print “Fizz” instead of the number


def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0:
            print("Fizz")
        else:
            print(i)


fizzbuzz()
