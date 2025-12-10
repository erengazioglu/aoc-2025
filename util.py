def read_input(filename, type="lines"):
    with open(filename, 'r') as f:
        match type:
            case "lines":
                return f.read().splitlines()
            case "commas":
                return f.read().split(",")

def replace_index(s:str, i:int, c:str) -> str:
    return s[:i] + c + s[i+1:]

def multiply(*args):
    acc = 1
    for num in args:
        acc *= num
    return acc

def add(*args):
    acc = 0
    for num in args:
        acc += num
    return acc