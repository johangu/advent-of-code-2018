def main():
    with open("day03.input") as f:
        claims = f.readlines()

    print("part01:", part01(claims))
    print("part02:", part02(claims))


def part01(claims):
    squares = {}
    for claim in claims:
        id, _, position, size = claim.split(' ')
        x, y = position[0:-1].split(',')
        width, height = size.split('x')
        map_squares(squares, x, y, width, height)
    return len([val for key, val in squares.items() if val > 1])


def part02(claims):
    squares = {}
    for claim in claims:
        id, _, position, size = claim.split(' ')
        x, y = position[0:-1].split(',')
        width, height = size.split('x')
        map_squares(squares, x, y, width, height)
    for claim in claims:
        id, _, position, size = claim.split(' ')
        x, y = position[0:-1].split(',')
        width, height = size.split('x')
        if not has_overlap(squares, x, y, width, height):
            return id


def has_overlap(squares, x, y, width, height):
    for i in range(int(width)):
        for j in range(int(height)):
            x_pos = int(x) + i
            y_pos = int(y) + j
            pos = (x_pos, y_pos)
            if squares[pos] != 1:
                return True
    return False


def map_squares(squares, x, y, width, height):
    for i in range(int(width)):
        for j in range(int(height)):
            x_pos = int(x) + i
            y_pos = int(y) + j
            pos = (x_pos, y_pos)
            squares[pos] = squares.setdefault(pos, 0) + 1
    return squares


if __name__ == "__main__":
    main()
