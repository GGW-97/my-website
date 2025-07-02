def solve_and_format(grid_str):
    # Replace this with your real solving logic
    grid = grid_str.strip().splitlines()
    solved = []
    for row in grid:
        solved.append("".join(c if c != '0' else '.' for c in row))
    return "\n".join(solved)