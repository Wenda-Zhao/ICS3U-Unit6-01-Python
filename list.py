#!/usr/bin/env python3

# Created by: Wenda Zhao
# Created on: Jan 2021
# This program for list


def main():
    # This function is for list

    import random
    my_numbers = []
    some_variable_plus = 0

    # process
    for loop_number in range(0, 10):
        some_variable = random.randint(0, 100)
        my_numbers.append(some_variable)
        some_variable_plus = some_variable_plus + some_variable
    average = some_variable_plus/10
    for loop_number in range(0, 10):
        print("The number is: {0}".format(my_numbers[loop_number]))
    print("")
    print("The average is: {0}".format(average))


if __name__ == "__main__":
    main()
