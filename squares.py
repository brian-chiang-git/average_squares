"""Computation of weighted average of squares."""

from argparse import ArgumentParser

import numpy as np

def average_of_squares(numbers_fromfile, weights_fromfile=None):
    """ Return the weighted average of a list of values.
    
    By default, all values are equally weighted, but this can be changed
    by the list_of_weights argument.
    
    Example:
    --------
    >>> average_of_squares([1, 2, 4])
    7.0
    >>> average_of_squares([2, 4], [1, 0.5])
    8.0
    >>> average_of_squares([1, 2, 4], [1, 0.5])
    Traceback (most recent call last):
    AssertionError: weights and numbers must have same length

    """
    list_of_numbers = np.loadtxt(numbers_fromfile, dtype=float, delimiter=',')
    list_of_weights = np.loadtxt(weights_fromfile, dtype=float, delimiter=',')
    if list_of_weights is not None:
        assert len(list_of_weights) == len(list_of_numbers), \
            "weights and numbers must have same length"
        effective_weights = list_of_weights
    else:
        effective_weights = [1] * len(list_of_numbers)
    squares = [
        weight * number * number
        for number, weight
        in zip(list_of_numbers, effective_weights)
    ]
    return sum(squares)/sum(effective_weights)


def convert_numbers(list_of_strings):
    """Convert a list of strings into numbers, ignoring whitespace.
    
    Example:
    --------
    >>> convert_numbers(["4", " 8 ", "15 16", " 23    42 "])
    [4, 8, 15, 16, 23, 42]

    """
    all_numbers = []
    for s in list_of_strings:
        # Take each string in the list, split it into substrings separated by
        # whitespace, and collect them into a single list...
        all_numbers.extend([token.strip() for token in s.split()])
    # ...then convert each substring into a number
    return [int(number_string) for number_string in all_numbers]

def process():
    parser = ArgumentParser(description="Calculate weighted squares of the given numbers")
    # parser.add_argument("numbers", type=float, nargs='+', help="Numbers to square and sum.")
    # parser.add_argument('--weights', '-w', type=float, nargs='+', help="Weights for the numbers.")
    parser.add_argument("numbers_fromfile", nargs='?', default="numbers.txt", help="Numbers to square and sum.")
    parser.add_argument('--weights_fromfile', '-w', nargs='?', default="weights.txt", help="Weights for the numbers.")
    args = parser.parse_args()

    print(average_of_squares(args.numbers_fromfile, args.weights_fromfile))

if __name__ == "__main__":
    process()
