import day01, day02, day03, day04
import argparse, os, shutil, sys

def new_day(num, force=False):
    day = f"day{num:02d}"

    if os.path.exists(day):
        if args.force:
            print(f"WARNING: Existing '{day}' directory has been overwritten (-f flag enabled).")
            shutil.rmtree(day, ignore_errors=True)
        else:
            print(f"ERROR: Directory '{day}' already exists. Aborting.", file=sys.stderr)
            sys.exit(1)

    os.makedirs(day)
    for filename in os.listdir("template"):
        src = os.path.join("template", filename)
        dst = os.path.join(day, filename)
        with open(src, 'r') as f_in:
            content = f_in.read().replace("{{DAY}}", str(num))
            with open(dst, 'w') as f_out:
                f_out.write(content)
    print(f"Created directory '{day}' from template.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code 2025")
    parser.add_argument('-t', '--test', action='store_true', help='Run tests')
    parser.add_argument('-s', '--sample', action='store_true', help='Use sample data instead of full version')
    parser.add_argument('-v', '--verbose', action='store_true', help='Print extra information')
    parser.add_argument('-n', '--new', type=int, help='Create a new day from template (e.g. --new 4)')
    parser.add_argument('-f', '--force', action='store_true', help='Used with "--new" to overwrite existing solution.')
    args = parser.parse_args()

    puzzle_input = "full"
    if args.new:
        new_day(args.new, args.force)
        sys.exit(0)
    if args.sample:
        puzzle_input = "sample"
    if args.test:
        # day01.tests.suite()
        # day02.tests.suite(args.verbose)
        day04.tests.suite()
    else:
        print(f"Verbose: {args.verbose}")
        # print("Day 01 | Part 1:", day01.part1(f"inputs/01-{puzzle_input}"))
        # print("Day 01 | Part 2:", day01.part2(f"inputs/01-{puzzle_input}"))
        # print("Day 02 | Part 1:", day02.part1(f"inputs/02-{puzzle_input}"))
        # print("Day 02 | Part 2:", day02.part2(f"inputs/02-{puzzle_input}", args.verbose))
        # print("Day 03 | Part 1:", day03.part1(f"inputs/03-{puzzle_input}", args.verbose))
        # print("Day 03 | Part 2:", day03.part2(f"inputs/03-{puzzle_input}", args.verbose))
        # print("Day 04 | Part 1:", day04.part1(f"inputs/04-{puzzle_input}", args.verbose))
        print("Day 04 | Part 2:", day04.part2(f"inputs/04-{puzzle_input}", args.verbose))

