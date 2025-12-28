with open("04/complex.txt") as f:
    grid = [elem.strip() for elem in f.readlines()]


def _is_hashtag(grid_elem: str):
    return grid_elem == "@"


def is_valid_hashtag(grid_line: list, line_index: int):
    if line_index < 0 or line_index >= len(grid_line):
        return False

    return _is_hashtag(grid_line[line_index])


def run_one_paper_removal(grid):
    hashtag_count = 0
    hashtag_coordinates = []
    for grid_index in range(len(grid)):
        grid_line = grid[grid_index]

        for elem_index in range(len(grid_line)):
            elem = grid_line[elem_index]
            if not _is_hashtag(elem):
                continue

            local_papers_close = 0
            if grid_index > 0:
                previous_line = grid[grid_index - 1]
                for previous_elem_index in [elem_index - 1, elem_index, elem_index + 1]:
                    if is_valid_hashtag(previous_line, previous_elem_index):
                        local_papers_close += 1

            for current_elem_index in [elem_index - 1, elem_index + 1]:
                if is_valid_hashtag(grid_line, current_elem_index):
                    local_papers_close += 1

            if grid_index < len(grid) - 1:
                next_line = grid[grid_index + 1]
                for next_elem_index in [elem_index - 1, elem_index, elem_index + 1]:
                    if is_valid_hashtag(next_line, next_elem_index):
                        local_papers_close += 1

            if local_papers_close < 4:
                hashtag_coordinates.append((grid_index, elem_index))
                hashtag_count += 1

    return hashtag_count, hashtag_coordinates


run_count, run_changes = run_one_paper_removal(grid)

result = run_count
while run_count > 0:
    for elem in run_changes:
        grid[elem[0]] = grid[elem[0]][: elem[1]] + "x" + grid[elem[0]][elem[1] + 1 :]

    run_count, run_changes = run_one_paper_removal(grid)

    result += run_count


print(result)
