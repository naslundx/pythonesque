#include <iostream>

def print(int i):
    if i > 3:
        while i > 0:
            std::cout << i << " "
            i -= 1
        std::cout << "\n"

def main():
    x = 0
    y = 10

    while x < y:
        x += 1
        print(x)

    return 0
