# Advent of Code 2025

Solutions for [Advent of Code 2025](https://adventofcode.com/2025) puzzles in Python.

## Structure

Each day's puzzle is in its own directory:
```
day01/
  solution.py    # Python solution
  input.txt      # Puzzle input
day02/
  solution.py
  input.txt
...
```

## Getting Started

### For a new day:

1. Copy the template:
   ```bash
   cp -r template.py dayXX/solution.py
   ```

2. Create the day directory and input file:
   ```bash
   mkdir dayXX
   touch dayXX/input.txt
   ```

3. Paste your puzzle input into `dayXX/input.txt`

4. Implement your solution in `dayXX/solution.py`

5. Run your solution:
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
- The `read_input()` function reads your puzzle input from `input.txt`
- Keep it simple - just plain Python, no fancy frameworks needed!
