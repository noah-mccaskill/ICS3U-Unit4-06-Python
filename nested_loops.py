#!/usr/bin/env python3

# Created by Noah McCaskill
# Created May 2022
# This program prints all the possible RGB values.


def main():
    # this function prints all possible RGB values.
    red = 0
    green = 0
    blue = 0

    # process, output
    for red in range(256):
        for green in range(256):
            for blue in range(256):
                print("RGB({0},{1},{2})".format(red, green, blue))

    print("\nDone.")


if __name__ == "__main__":
    main()
