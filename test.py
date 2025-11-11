from a5 import Board, remove_if_exists, DFS, BFS

# Recreated tests with changed integers
first_moves = [
    (0, 1, 5),
    (0, 7, 3),
    (1, 2, 4),
    (1, 3, 9),
    (1, 5, 6),
    (1, 6, 1),
    (2, 2, 7),
    (2, 3, 5),
    (2, 6, 8),
    (3, 1, 2),
    (3, 2, 9),
    (3, 4, 4),
    (4, 1, 8),
    (4, 3, 6),
    (4, 5, 3),
    (4, 7, 2),
    (5, 4, 5),
    (5, 6, 9),
    (5, 7, 7),
    (6, 2, 6),
    (6, 5, 8),
    (6, 6, 2),
    (7, 2, 3),
    (7, 3, 7),
    (7, 5, 1),
    (7, 6, 5),
    (8, 1, 4),
    (8, 7, 9),
]

# Part 1 tests
b = Board()
for trip in first_moves:
    b.rows[trip[0]][trip[1]] = trip[2]

# make some lists shorter to create constrained cells
remove_if_exists(b.rows[0][0], 8)
remove_if_exists(b.rows[0][0], 7)
remove_if_exists(b.rows[0][0], 3)
remove_if_exists(b.rows[0][0], 2)
remove_if_exists(b.rows[4][8], 8)
remove_if_exists(b.rows[4][8], 1)
remove_if_exists(b.rows[4][8], 2)
remove_if_exists(b.rows[4][8], 3)
remove_if_exists(b.rows[4][8], 4)
remove_if_exists(b.rows[6][7], 2)
remove_if_exists(b.rows[6][7], 3)
remove_if_exists(b.rows[6][7], 5)
remove_if_exists(b.rows[6][7], 6)

assert b.find_most_constrained_cell() == (4, 8), "find most constrained cell test 1"
assert b.failure_test() == False, "failure test test 1"
assert b.goal_test() == False, "goal test test 1"

b.rows[4][3] = []
assert b.find_most_constrained_cell() == (4, 3), "find most constrained cell test 2"
assert b.failure_test() == True, "failure test test 2"
print("All part 1 tests passed!")

# Part 2 tests (update)
g = Board()
for trip in first_moves:
    g.update(trip[0], trip[1], trip[2])

assert g.rows[0][2] == [2, 5, 6], "update test 1"
assert g.rows[5][5] == [3, 7, 9], "update test 2"
assert g.num_nums_placed == 28, "update test 3"
assert g.find_most_constrained_cell() == (1, 7), "fmc test"
assert g.failure_test() == False, "failure test test"
assert g.goal_test() == False, "goal test test"

# goal_test true when num_nums_placed artificially set
g.num_nums_placed = 81
assert g.goal_test() == True, "goal test test"
print("All part 2 tests passed!")

print("All tests in test_a5.py passed!")