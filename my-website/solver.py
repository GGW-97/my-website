def solve_and_format(grid_str):
    # Replace this with your real solving logic
    print(grid_str)
    grid = grid_str.strip().splitlines()
    solved = []
    for row in grid:
        solved.append("".join(c if c != '0' else '.' for c in row))
    return "\n".join(solved)