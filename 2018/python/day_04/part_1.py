import numpy
import re
import datetime


class Guard():
    def __init__(self, date, tag):
        self.tag = tag
        self.dates = {}
        self.add_date(date)

    def __repr__(self):
        lines = []
        for date, values in self.dates.items():
            timeline = "".join(map(str, values[0]))
            lines.append(f"{date} #{self.tag} {timeline}")

        return "\n".join(lines)

    def table(self):
        rows = []
        for _, row in sorted(self.dates.items()):
            rows.append(row)

        return numpy.concatenate(rows, axis=0)

    def add_date(self, date):
        day = numpy.ndarray(shape=(1, 60), dtype=numpy.int32)
        day[:, :] = 0
        self.dates[date] = day

    def sleep(self, date, minute):
        self.sleep_minute = minute

    def wake_up(self, date, minute):
        self.wake_up_minute = minute
        self.dates[date][0, self.sleep_minute:self.wake_up_minute] = 1

    def has_slept(self):
        slept = 0
        for values in self.dates.values():
            slept += numpy.sum(values)

        return slept

    def max_minute(self):
        table = self.table()
        minute = numpy.argmax(numpy.average(table, axis=0))
        amount = numpy.sum(table[:, minute])
        return (minute, amount)

def log(log_lines):
    tag = ''
    guards = {}
    for line in log_lines:
        date_string = re.search(r'.*\[([0-9]{4}-[0-9]{2}-[0-9]{2}) ([0-9]{2}):([0-9]{2})\].*', line)
        date = date_string.group(1)
        hour = int(date_string.group(2))
        minute = int(date_string.group(3))
        if hour != 0:
            date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
            date += datetime.timedelta(days=1)
            date = str(date)
            minute = 0

        if 'Guard' in line:
            tag = int(re.search('.*Guard #([0-9]+).*', line).group(1))
            if tag not in guards:
                guards[tag] = Guard(date, tag)

            else:
                guards[tag].add_date(date)

        if  'asleep' in line:
            guards[tag].sleep(date, minute)

        if 'wakes' in line:
            guards[tag].wake_up(date, minute)

    return guards

def sleepy_guard(guards):
    slept = {}
    for guard in guards.values():
        slept[guard.has_slept()] = guard.tag

    max_slept = max(slept.keys())
    return slept[max_slept]

def find_minute(table):
    return numpy.argmax(numpy.sum(table, axis=0))

def sort_log(sequences):
    log_lines = {}
    for line in sequences:
        date_string = re.search(r'.*\[([0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2})\].*', line)
        date = date_string.group(1)
        date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M')
        log_lines[date] = line

    lines = []
    for date, line in sorted(log_lines.items()):
        lines.append(line)

    return lines


def solution(sequences):
    """Solution to part one.
    """
    sorted_log = sort_log(sequences)
    guards = log(sorted_log)
    suspect = sleepy_guard(guards)
    table = guards[suspect].table()
    minute = find_minute(table)
    print(f"sleepy guard {suspect} slept for {guards[suspect].has_slept()}")
    print(f"most at minute {minute}")
    print(f"answer: {suspect * minute}")
    return suspect * minute
