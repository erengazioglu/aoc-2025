import day01, day02
import argparse

# def main():

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code 2025")
    parser.add_argument('-t', '--test', action='store_true', help='Run tests')
    parser.add_argument('-s', '--sample', action='store_true', help='Use sample data instead of full version')
    parser.add_argument('-v', '--verbose', action='store_true', help='Print extra information')
    args = parser.parse_args()

    puzzle_input = "full"
    if args.sample:
        puzzle_input = "sample"
    if args.test:
        day01.tests.suite()
        day02.tests.suite(args.verbose)
    else:
        print(f"Verbose: {args.verbose}")
        print("Day 01 | Part 1:", day01.part1(f"inputs/01-{puzzle_input}"))
        print("Day 01 | Part 2:", day01.part2(f"inputs/01-{puzzle_input}"))
        print("Day 02 | Part 1:", day02.part1(f"inputs/02-{puzzle_input}"))
        print("Day 02 | Part 2:", day02.part2(f"inputs/02-{puzzle_input}", args.verbose))
