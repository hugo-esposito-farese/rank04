def constellation_mapper(stars: list[tuple[int, int]], size: int) -> list[str]:
    grid = [["." for _ in range(size)] for _ in range(size)]
    for row, col in stars:
        if 0 <= row < size and 0 <= col < size:
            grid[row][col] = "*"
    return ["".join(line) for line in grid]
