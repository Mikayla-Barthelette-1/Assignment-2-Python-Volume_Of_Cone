#!/usr/bin/env python3

# Created by: Mikayla Barthelette
# Created on: Sept 2021
# This program finds the volume of a cone

import math


def main():
    # this function calculates the volume

    # input
    radius = int(input("Enter the radius of the cone (mm): "))
    height = int(input("Enter the height of the cone (mm): "))

    # process
    volume = math.pi * radius ** 2 * (height / 3)

    # output
    print("\nThe volume of the cone is: {0} mm³.".format(volume))
    
    print("\nDone.")


if __name__ == "__main__":
    main()
