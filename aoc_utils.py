"""
Utility functions for Advent of Code 2025
"""

def read_input(filename='input.txt'):
    """Read and return the puzzle input."""
    with open(filename, 'r') as f:
        return f.read().strip()
