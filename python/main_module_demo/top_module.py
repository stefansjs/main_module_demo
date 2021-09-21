#!/usr/bin/env python3

import sys

def print_main_package():
    print(sys.modules['__main__'].__package__)


if __name__ == '__main__':
    print_main_package()
