from string import ascii_uppercase


def main():
    with open('day05.input') as f:
        polymer = f.read()[:-1]  # remove linebreak

    print('part01:', part01(polymer))
    print('part02:', part02(polymer))


def part01(polymer):
    reacted = react(polymer)
    return len(reacted)


def react(polymer):
    reacted = None
    for c in polymer:
        if reacted is None:
            reacted = c
        if c.swapcase() == reacted[-1]:
            reacted = reacted[:-1]
        else:
            reacted += c

    return reacted


def part02(polymer):
    shortest = None
    for c in ascii_uppercase:
        test_string = polymer.replace(c, '').replace(c.lower(), '')
        reacted = react(test_string)
        if shortest is None:
            shortest = reacted
        elif len(reacted) < len(shortest):
            shortest = reacted

    return len(shortest)


if __name__ == "__main__":
    main()
