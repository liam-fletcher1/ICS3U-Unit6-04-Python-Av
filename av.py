#!/usr/bin/env python3

# Created by: Liam Fletcher
# Created on: Oct 2021
# This program uses a 2D array to find the average of numbers

import random


def av_numbers(grid, rows, columns):
    # this function adds up all the numbers in  a 2D array

    total = 0
    for row_val in grid:
        for arr_element in row_val:
            total += arr_element
    total = total / (rows * columns)

    return total


def main():
    # this function uses a 2D array

    list_2d = []

    # input
    rows = input("How many row would you like: ")
    columns = input("How many columns would you like: ")
    print("")

    try:
        rows_int = int(rows)
        columns_int = int(columns)

        for loop_counter_rows in range(0, rows_int):
            temp_col = []
            for loop_counter_columns in range(0, columns_int):
                random_number = random.randint(0, 50)
                temp_col.append(random_number)
                print("{0} ".format(random_number), end="")
            list_2d.append(temp_col)
            print("")

        answer = av_numbers(list_2d, rows_int, columns_int)
        if rows_int < 0:
            print("These are invaild numbers.")
        else:
            print("")
            print("The average of all the numbers is: {0} ".format(answer))

    except Exception:
        print("These are invaild numbers.")

    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
