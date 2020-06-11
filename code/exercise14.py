from dateutil.parser import parse


def date_delta(start, end):
    a = parse(start)
    b = parse(end)
    return (b - a).total_seconds()


start = input()  # sys.stdin.readline()
end = input()  # sys.stdin.readline()

print(date_delta(start, end))