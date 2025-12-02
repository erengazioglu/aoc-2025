# Advent of Code 2025

Solutions for [Advent of Code 2025](https://adventofcode.com/2025) puzzles in Python.

## Structure

Each day's puzzle is in its own directory:
```
aoc_utils.py         # Shared utility functions
template.py          # Template for new days
day01/
  solution.py        # Python solution
  input.txt          # Puzzle input
day02/
  solution.py
  input.txt
...
```

## Getting Started

### For a new day:

1. Create the day directory:
   ```bash
   mkdir dayXX
   ```

2. Copy the template:
   ```bash
   cp template.py dayXX/solution.py
   ```

3. Create the input file:
   ```bash
   touch dayXX/input.txt
   ```

4. Paste your puzzle input into `dayXX/input.txt`

5. Implement your solution in `dayXX/solution.py`

6. Run your solution:
   ```bash
   cd dayXX
   python solution.py
   ```

## Example

Day 1 is already set up as an example:
```bash
cd day01
python solution.py
```

## Tips

- Each day has two parts - implement them in `part1()` and `part2()` functions
- The `read_input()` function is imported from `aoc_utils.py` and reads your puzzle input from `input.txt`
- Keep it simple - just plain Python, no fancy frameworks needed!
