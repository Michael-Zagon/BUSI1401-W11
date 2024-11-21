#!/usr/bin/env python3

# Created by: Michael Zagon
# Created on: Nov 2024
# This program finds the volume of a cube

def cube_volume_calculation(side_length):
    volume = side_length ** 3
    return volume


def main():
    # Input
    side_length = input("Enter the length of one side of the cube (cm): ")

    try:
        side_length = float(side_length)

        final_volume = cube_volume_calculation(side_length)
        print(
            "\nThe volume of a cube with side length {0} cm is {1} cm.".format(
                side_length, final_volume
            )
        )
    except ValueError:
        print("\nInvalid Input. Please enter a numerical value.")


if __name__ == "__main__":
    main()