#!/usr/bin/env python3

# Created by: Michael Zagon
# Created on: Nov 2024
# This program calculates savings account numbers

rate = 1.05
balance = 1000

for i in range (1,6):
    Nbalance = balance * rate
    print("Year", i , "\t", Nbalance,)