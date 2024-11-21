#!/usr/bin/env python3

# Created by: Michael Zagon
# Created on: Nov 2024
# This program finds the sum and average of the given numbers

# Initializing Variables
total = 0
count = 0

salary = 0



while salary >= 0:
    salary = float(input("Enter your salary (-1 to stop): "))
    if salary >= 0:
        total = total + salary
        count = count + 1


if count > 0:
    average = total / count
    print(f"The average salary is", {average})
else:
    print("No data entered")
