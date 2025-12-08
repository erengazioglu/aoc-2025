def read_input(filename, type="lines"):
    with open(filename, 'r') as f:
        match type:
            case "lines":
                return f.read().splitlines()
            case "commas":
                return f.read().split(",")