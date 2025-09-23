
def create_file(name):
    with open(name, "x", encoding="utf-8") as f:
        f.write("")
    return True

def write_file(name, data):
    with open(name, "w", encoding="utf-8") as f:
        f.write(data)
    return True

def read_file(name):
    with open(name, "r", encoding="utf-8") as f:
        return f.read()

def append_file(name, data):
    with open(name, "a", encoding="utf-8") as f:
        f.write(data)
    return True
