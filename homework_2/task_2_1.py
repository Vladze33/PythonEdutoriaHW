def is_float(element: any) -> bool:
    if element is None: 
        return False
    try:
        float(element)
        return True
    except ValueError:
        return False


def read_file_numbers(path):
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in map(lambda l: l.strip(), lines):
            # if not line.isdecimal(): # Only natural numbers
            if not is_float(line):
                raise TypeError(f'"{line}" is not a number')
            print(line)


try:
    read_file_numbers("file.txt")
except FileNotFoundError as e:
    print(e)
except TypeError as e:
    print(e)
