#!/usr/bin/env python3
# Created By: Kaylee Ralejoe
# Date: 09,10,2026
# The program calculates the total
# surface area and volume of
# a cone with a given radius, vertical height and
# slanted height from the user
# and displays the results to the user

import math


def main():
    # greet the user
    print("Welcome, let us calculate the total surface area and volume of a cone!")

    # ask the user to enter the radius
    radius = float(input("Enter the radius of the cone base (cm): "))

    # ask user to enter the vertical height
    v_height = float(input("Enter the vertical height of the cone (cm): "))

    # calculate the slanted height based on user input
    s_height = math.sqrt(radius**2 + v_height**2)

    # calculate the area of the cone
    total_surface_area = (math.pi * radius**2) + (math.pi * radius * s_height)

    # calculate the volume of the cone
    volume = 1 / 3 * math.pi * radius**2 * v_height

    # display the area and volume of the cone
    print(
        "The total surface area of the cone is = {:.2f}cm²".format(total_surface_area)
    )
    print("The volume of the cone is = {:.2f}cm³".format(volume))


if __name__ == "__main__":
    main()
