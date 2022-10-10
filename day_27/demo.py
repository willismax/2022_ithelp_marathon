import sys


def get_sys_platform():
    platform = sys.platform
    return platform


def add(num1, num2):
    return num1 + num2


def calculate(num1, num2):
    add_result = add(num1=num1, num2=num2)

    return add_result
