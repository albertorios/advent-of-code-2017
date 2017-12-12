from itertools import cycle


def cycle_string(s, offset):
    c = cycle(s)
    for i in range(offset):
        next(c)

    return [next(c) for i in range(len(s))]


def inverse_captcha_sum(digits_string, offset=1):
    d_cycle = cycle_string(digits_string, offset)

    return sum([int(x) for x, y in list(zip(digits_string, d_cycle))
               if x == y])


def part_one(digits_string):
    return inverse_captcha_sum(digits_string, 1)


def part_two(digits_string):
    return inverse_captcha_sum(digits_string, len(digits_string) // 2)


if __name__ == '__main__':
    with open('puzzle_input.txt', 'r') as f:
        puzzle_input = f.readline().strip()

    # part one solution
    print(part_one(puzzle_input))

    # part two solution
    print(part_two(puzzle_input))
