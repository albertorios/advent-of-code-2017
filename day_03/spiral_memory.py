from itertools import cycle


def move_position(p, m):
    return (p[0] + m[0], p[1] + m[1])


def create_grid(value_func):
    grid = {}

    moves = cycle([(1, 0), (0, -1), (-1, 0), (0, 1)])  # right, up, left, down
    last_move = None
    next_move = next(moves)

    position = (0, 0)

    while True:
        if last_move:
            while(position in grid):
                next_position = move_position(position, next_move)

                if next_position in grid:
                    position = move_position(position, last_move)
                else:
                    position = next_position
                    last_move = next_move
                    next_move = next(moves)
        else:
            last_move, next_move = next_move, next(moves)

        value = value_func(grid, position)
        grid[position] = value

        yield(position[0], position[1], value)


def index_identity(grid, position=None):
    return len(grid) + 1


def adjacent_sum(grid, position):
    if position == (0, 0):
        return 1

    adj_positions = [(-1, -1), (0, -1), (1, -1),
                     (-1, 0), (1, 0),
                     (-1, 1), (0, 1), (1, 1)]
    adj_positions = [move_position(position, p) for p in adj_positions]
    values = [grid.get(p, 0) for p in adj_positions]

    return sum(values)


def part_one(n):
    grid = create_grid(index_identity)
    last_position = [next(grid) for i in range(n)][-1]

    return abs(last_position[0]) + abs(last_position[1])


def part_two(n):
    grid = create_grid(adjacent_sum)
    val = next(grid)[-1]

    while val < n:
        val = next(grid)[-1]

    return val


if __name__ == '__main__':
    puzzle_input = 347991
    print(part_one(puzzle_input))
    print(part_two(puzzle_input))
