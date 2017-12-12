def read_input():
    with open('puzzle_input.txt', 'r') as f:
        return [list(map(int, l.strip().split())) for l in f.readlines()]


def checksum(input_arr, row_func):
    return sum([row_func(row) for row in input_arr])


def max_minus_min(row):
    xs = sorted(row)
    return xs[-1] - xs[0]


def even_divisibility(row):
    xs = sorted(row)
    for i, x in enumerate(xs):
        for y in xs[i + 1:]:
            if y % x == 0:
                return y // x


def part_one(input_arr):
    return checksum(input_arr, max_minus_min)


def part_two(input_arr):
    return checksum(input_arr, even_divisibility)


if __name__ == '__main__':
    input_arr = read_input()

    # part one solution
    print(part_one(input_arr))
    # part two solution
    print(part_two(input_arr))
