from collections import defaultdict


def main():
    with open('day04.input') as f:
        lines = f.read().splitlines()
        lines.sort()

    sleep_log, totals = parse_logs(lines)
    print('part01:', part01(sleep_log, totals))
    print('part02:', part02(sleep_log))


def parse_logs(lines):
    id = None
    asleep_at = None
    sleep_log = defaultdict(int)
    totals = defaultdict(int)

    for line in lines:
        if line:
            minute = parse_minute(line)
            if "begins shift" in line:
                id = int(line.split()[3][1:])
            elif "falls asleep" in line:
                asleep_at = minute
            elif "wakes up" in line:
                for i in range(asleep_at, minute):
                    sleep_log[(id, i)] += 1
                    totals[id] += 1
                asleep_at = None

    return (sleep_log, totals)


def parse_minute(line):
    time = line.split()[1][:-1]
    return int(time.split(':')[1])


def find_best_minute(sleep_log, id):
    best = None
    for (guard, minute), value in sleep_log.items():
        if guard == id:
            if best is None or value > sleep_log[(id, best)]:
                best = minute
    return best


def find_best_guard_and_minute(sleep_log):
    best = None
    for k, v in sleep_log.items():
        if best is None or v > sleep_log[best]:
            best = k
    return best


def part01(sleep_log, totals):
    best_guard = max(totals, key=lambda k: totals[k])
    best_minute = find_best_minute(sleep_log, best_guard)
    return int(best_guard) * int(best_minute)


def part02(sleep_log):
    best_guard, best_minute = find_best_guard_and_minute(sleep_log)
    return int(best_guard) * int(best_minute)


if __name__ == "__main__":
    main()
