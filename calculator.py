"""A four-function calculator. The tests in test_calculator.py check it."""


def add(a, b):
    # Classroom demo: this line is correct, so the workflow stays green.
    # Change it to `return a - b`, commit, and push. The Actions tab
    # will mark the test job with a red X and name the test that failed.
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("cannot divide by zero")
    return a / b
