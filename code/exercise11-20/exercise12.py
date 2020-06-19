import sys
import datetime
from datetime import datetime, date, timedelta


def next_day(date_str):
    today = datetime.strptime(date_str, '%Y-%m-%d')
    tomorrow = today + timedelta(days=1)
    return str(tomorrow)[:10]


def prev_day(date_str):
    today = datetime.strptime(date_str, '%Y-%m-%d')
    yesterday = today + timedelta(days=-1)
    return str(yesterday)[:10]


while True:
    line = sys.stdin.readline()
    line = line.strip()
    if line == '':
        break
    print('前一天:', prev_day(line))
    print('后一天:', next_day(line))