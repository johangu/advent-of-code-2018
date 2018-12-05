twice = {}
thrice = {}


def part01(ids):
    for id in ids:
        for c in id:
            count = id.count(c)
            if count == 2:
                twice[id] = True
            elif count == 3:
                thrice[id] = True
    return len(twice) * len(thrice)


def part02():
    ids = [*twice] + [*thrice]
    for i in range(len(ids) - 1):
        for j in range(i + 1, len(ids) - 1):
            if hamming_distance(ids[i], ids[j]) == 1:
                return ''.join(c for c, c2 in zip(ids[i], ids[j]) if c == c2)


def hamming_distance(x, y):
    return sum(c1 != c2 for c1, c2 in zip(x, y))


if __name__ == "__main__":
    with open('day02.input') as f:
        ids = f.readlines()

    print("part 1:", part01(ids))
    print("part 2:", part02())
