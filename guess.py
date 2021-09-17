#!/usr/bin/env python3

# Created by: Haokai Li
# Created on: Sept 2021
# This Program guess a number between 0 - 9


def main():
    # This function guess a number between 0 - 9

    # input
    number = int(input("Enter a number between 0 - 9: "))
    print("")

    # process
    if number == 5:
        # output
        print("You guessed correctly!")

    if number != 5:
        # output
        print("You guessed wrong!")

    print("\nDone")


if __name__ == "__main__":
    main()
