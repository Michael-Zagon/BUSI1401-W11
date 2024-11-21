#!/usr/bin/env python3

# Created by: Michael Zagon
# Created on: Nov 2024
# This script finds how long it takes for a deposit to double in value

balance = float(input("Please input the initial balance: "))
rate = float(input("Please input the interest rate in decimal form:"))

target = 2 * balance
year = 0

while balance < target:
    year = year + 1
    balance = balance * (1+rate)

print("It would take {0} years to double your balance.".format(year))