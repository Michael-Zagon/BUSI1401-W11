#!/usr/bin/env python3

# Created by: Michael Zagon
# Created on: Nov 2024
# This program prints a bar using * or #

def evenBar(even_num):
    num = even_num //2
    print("*"*num)

def oddBar(odd_num):
    num = odd_num
    print("#"*num)

def main():
    num = int(input("Please input the number: "))
    if num%2 == 0:
        evenBar(num)
    else:
        oddBar(num)

if __name__ == "__main__":
    main()