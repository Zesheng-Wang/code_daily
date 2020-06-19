import sys


def convert_to_seconds(time_str):
    # write code here
    s = time_str[:-1]
    character = time_str[-1]
    if character == 's':
        return float(s)
    elif character == 'm':
        return float(s) * 60
    elif character == 'h':
        return float(s) * 60 * 60
    elif character == 'd' or character == 'D':
        return float(s) * 60 * 60 * 24


while True:
    line = sys.stdin.readline()
    line = line.strip()
    if line == '':
        break
    print(convert_to_seconds(line))
