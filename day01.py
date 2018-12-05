def part01(frequencies):
    return sum(int(x) for x in frequencies)


def part02(frequencies):
    seen_frequencies = {0: True}
    current_frequency = 0

    while True:
        for frequency in frequencies:
            current_frequency = current_frequency + int(frequency)
            if seen_frequencies.setdefault(current_frequency, False):
                return current_frequency
            else:
                seen_frequencies[current_frequency] = True


if __name__ == "__main__":
    with open('day01.input') as f:
        frequencies = f.readlines()

    print("part 1:", part01(frequencies))
    print("part 2:", part02(frequencies))
