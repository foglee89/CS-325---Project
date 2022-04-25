# AUTHOR: Erik Fogle
# DATE: 03/01/22
# ONID: Foglee@oregonstate.edu
# ASSIGNMENT: HW 8
# DESCRIPTION: Program has a function that takes a puzzle of undefined size in the
#               form of a matrix, a starting point, and ending point. It determines if
#               a path exists between the two points and the minimum number of cells
#               that need to be visited to travel between them.

# ASSUMPTIONS: All puzzles passed will be minimum size of at least 3x3.

# EXTRA CREDIT: IMPLEMENTED, return value now a tuple that contains a string value that
#               represents a possible min path from the source to destination.

from heapq import heappop, heappush


def solve_puzzle(Board: list[list[str]], Source: tuple, Destination: tuple) -> tuple:
    """
    Description:
        Function takes a puzzle in the form of a matrix and determines the least amount
        of cells that need to be visited to go from the source cell to the destination
        cell. If no such path exists, None is returned. Open cell is denoted by '-' and
        blocked cell is denoted by '#'. Function returns the minimum number of cells visited
        and a possible minimum path (extra credit).

    Extra Credit:
        IMPLEMENTED, see above

    :param Board: matrix (list of lists) representing the puzzling looking to solve
    :param Source: tuple containing coordinate value for Source cell.
    :param Destination: tuple containing coordinate value for Destination cell.
    :return: Tuple containing; integer value for the minimum number of cells needed to visit to get
                from Source to Destination and a string value with the directions of a possible min
                path. If no such path exists, returns None.
    """
    check_coordinates = [(0, 1, 'R'), (1, 0, 'D'), (0, -1, 'L'), (-1, 0, 'U')]
    traveled_matrix = [[float('inf')] * (len(Board[0])) for _ in range(len(Board))]
    src_row, src_col = Source
    min_heap = [(0, src_row-1, src_col-1, '')]
    traveled_matrix[src_row-1][src_col-1] = 0
    visited = []
    dest_row, dest_col = Destination
    dest_coor = (dest_row-1, dest_col-1)

    while dest_coor not in visited and len(min_heap) > 0:
        dist, row, col, directions = heappop(min_heap)

        if (row, col) in visited:
            continue

        if row > 0 and col > 0:
            visited.append((row, col))

        if (row, col) == dest_coor:
            return dist - 1, directions

        for cc_row, cc_col, cc_dir in check_coordinates:
            check_row, check_col = row + cc_row, col + cc_col
            if not 0 <= check_row < len(Board) or not 0 <= check_col < len(Board[0]):
                continue
            if (check_row, check_col) in visited or Board[check_row][check_col] == '#':
                continue
            check_dist = max(dist, traveled_matrix[row][col] + 1)
            if check_dist < traveled_matrix[check_row][check_col]:
                traveled_matrix[check_row][check_col] = check_dist
                heappush(min_heap, (check_dist, check_row, check_col, directions + cc_dir))


# # Testing Code
# test_board = [['-', '-', '-', '-', '-'],
#               ['-', '-', '#', '-', '-'],
#               ['-', '-', '-', '-', '-'],
#               ['#', '-', '#', '#', '-'],
#               ['-', '#', '-', '-', '-']]
# test_start_1 = (1, 3)
# test_dest_1 = (3, 3)
# test_start_2 = (1, 1)
# test_dest_2 = (5, 5)
# test_start_3 = (1, 1)
# test_dest_3 = (5, 1)
#
# # Output: 3
# print(solve_puzzle(test_board, test_start_1, test_dest_1))
# # Output: 7
# print(solve_puzzle(test_board, test_start_2, test_dest_2))
# # Output: None
# print(solve_puzzle(test_board, test_start_3, test_dest_3))
