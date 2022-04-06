import random
R=[
[[0, 0],[0, 0, 0, 0]],
[[0, 0], [1, 0], [0, 1, 0, 0]],
[[0, 0], [1, 1], [0, 1, 0, 1]],
[[0, 0], [0, 1], [0, 0, 0, 1]],
[[0, 0], [-1, 1], [-1, 0, 0, 1]],
[[0, 0], [-1, 0], [-1, 0, 0, 0]],
[[0, 0], [-1, -1], [-1, 0, -1, 0]],
[[0, 0], [0, -1], [0, 0, -1, 0]],
[[0, 0], [1, -1], [0, 1, -1, 0]],
[[0, 0], [1, 0], [2, 0], [0, 2, 0, 0]],
[[0, 0], [1, 0], [2, 1], [0, 2, 0, 1]],
[[0, 0], [1, 0], [1, 1], [0, 1, 0, 1]],
[[0, 0], [1, 0], [0, 1], [0, 1, 0, 1]],
[[0, 0], [1, 0], [0, 0], [0, 1, 0, 0]],
[[0, 0], [1, 0], [0, -1], [0, 1, -1, 0]],
[[0, 0], [1, 0], [1, -1], [0, 1, -1, 0]],
[[0, 0], [1, 0], [2, -1], [0, 2, -1, 0]],
[[0, 0], [1, 1], [2, 1], [0, 2, 0, 1]],
[[0, 0], [1, 1], [2, 2], [0, 2, 0, 2]],
[[0, 0], [1, 1], [1, 2], [0, 1, 0, 2]],
[[0, 0], [1, 1], [0, 2], [0, 1, 0, 2]],
[[0, 0], [1, 1], [0, 1], [0, 1, 0, 1]],
[[0, 0], [1, 1], [0, 0], [0, 1, 0, 1]],
[[0, 0], [1, 1], [1, 0], [0, 1, 0, 1]],
[[0, 0], [1, 1], [2, 0], [0, 2, 0, 1]],
[[0, 0], [0, 1], [1, 1], [0, 1, 0, 1]],
[[0, 0], [0, 1], [1, 2], [0, 1, 0, 2]],
[[0, 0], [0, 1], [0, 2], [0, 0, 0, 2]],
[[0, 0], [0, 1], [-1, 2], [-1, 0, 0, 2]],
[[0, 0], [0, 1], [-1, 1], [-1, 0, 0, 1]],
[[0, 0], [0, 1], [-1, 0], [-1, 0, 0, 1]],
[[0, 0], [0, 1], [0, 0], [0, 0, 0, 1]],
[[0, 0], [0, 1], [1, 0], [0, 1, 0, 1]],
[[0, 0], [-1, 1], [0, 1], [-1, 0, 0, 1]],
[[0, 0], [-1, 1], [0, 2], [-1, 0, 0, 2]],
[[0, 0], [-1, 1], [-1, 2], [-1, 0, 0, 2]],
[[0, 0], [-1, 1], [-2, 2], [-2, 0, 0, 2]],
[[0, 0], [-1, 1], [-2, 1], [-2, 0, 0, 1]],
[[0, 0], [-1, 1], [-2, 0], [-2, 0, 0, 1]],
[[0, 0], [-1, 1], [-1, 0], [-1, 0, 0, 1]],
[[0, 0], [-1, 1], [0, 0], [-1, 0, 0, 1]],
[[0, 0], [-1, 0], [0, 0], [-1, 0, 0, 0]],
[[0, 0], [-1, 0], [0, 1], [-1, 0, 0, 1]],
[[0, 0], [-1, 0], [-1, 1], [-1, 0, 0, 1]],
[[0, 0], [-1, 0], [-2, 1], [-2, 0, 0, 1]],
[[0, 0], [-1, 0], [-2, 0], [-2, 0, 0, 0]],
[[0, 0], [-1, 0], [-2, -1], [-2, 0, -1, 0]],
[[0, 0], [-1, 0], [-1, -1], [-1, 0, -1, 0]],
[[0, 0], [-1, 0], [0, -1], [-1, 0, -1, 0]],
[[0, 0], [-1, -1], [0, -1], [-1, 0, -1, 0]],
[[0, 0], [-1, -1], [0, 0], [-1, 0, -1, 0]],
[[0, 0], [-1, -1], [-1, 0], [-1, 0, -1, 0]],
[[0, 0], [-1, -1], [-2, 0], [-2, 0, -1, 0]],
[[0, 0], [-1, -1], [-2, -1], [-2, 0, -1, 0]],
[[0, 0], [-1, -1], [-2, -2], [-2, 0, -2, 0]],
[[0, 0], [-1, -1], [-1, -2], [-1, 0, -2, 0]],
[[0, 0], [-1, -1], [0, -2], [-1, 0, -2, 0]],
[[0, 0], [0, -1], [1, -1], [0, 1, -1, 0]],
[[0, 0], [0, -1], [1, 0], [0, 1, -1, 0]],
[[0, 0], [0, -1], [0, 0], [0, 0, -1, 0]],
[[0, 0], [0, -1], [-1, 0], [-1, 0, -1, 0]],
[[0, 0], [0, -1], [-1, -1], [-1, 0, -1, 0]],
[[0, 0], [0, -1], [-1, -2], [-1, 0, -2, 0]],
[[0, 0], [0, -1], [0, -2], [0, 0, -2, 0]],
[[0, 0], [0, -1], [1, -2], [0, 1, -2, 0]],
[[0, 0], [1, -1], [2, -1], [0, 2, -1, 0]],
[[0, 0], [1, -1], [2, 0], [0, 2, -1, 0]],
[[0, 0], [1, -1], [1, 0], [0, 1, -1, 0]],
[[0, 0], [1, -1], [0, 0], [0, 1, -1, 0]],
[[0, 0], [1, -1], [0, -1], [0, 1, -1, 0]],
[[0, 0], [1, -1], [0, -2], [0, 1, -2, 0]],
[[0, 0], [1, -1], [1, -2], [0, 1, -2, 0]],
[[0, 0], [1, -1], [2, -2], [0, 2, -2, 0]],
[[0, 0], [1, 0], [2, 0], [3, 0], [0, 3, 0, 0]],
[[0, 0], [1, 0], [2, 0], [3, 1], [0, 3, 0, 1]],
[[0, 0], [1, 0], [2, 0], [2, 1], [0, 2, 0, 1]],
[[0, 0], [1, 0], [2, 0], [1, 1], [0, 2, 0, 1]],
[[0, 0], [1, 0], [2, 0], [1, 0], [0, 2, 0, 0]],
[[0, 0], [1, 0], [2, 0], [1, -1], [0, 2, -1, 0]],
[[0, 0], [1, 0], [2, 0], [2, -1], [0, 2, -1, 0]],
[[0, 0], [1, 0], [2, 0], [3, -1], [0, 3, -1, 0]],
[[0, 0], [1, 0], [2, 1], [3, 1], [0, 3, 0, 1]],
[[0, 0], [1, 0], [2, 1], [3, 2], [0, 3, 0, 2]],
[[0, 0], [1, 0], [2, 1], [2, 2], [0, 2, 0, 2]],
[[0, 0], [1, 0], [2, 1], [1, 2], [0, 2, 0, 2]],
[[0, 0], [1, 0], [2, 1], [1, 1], [0, 2, 0, 1]],
[[0, 0], [1, 0], [2, 1], [1, 0], [0, 2, 0, 1]],
[[0, 0], [1, 0], [2, 1], [2, 0], [0, 2, 0, 1]],
[[0, 0], [1, 0], [2, 1], [3, 0], [0, 3, 0, 1]],
[[0, 0], [1, 0], [1, 1], [2, 1], [0, 2, 0, 1]],
[[0, 0], [1, 0], [1, 1], [2, 2], [0, 2, 0, 2]],
[[0, 0], [1, 0], [1, 1], [1, 2], [0, 1, 0, 2]],
[[0, 0], [1, 0], [1, 1], [0, 2], [0, 1, 0, 2]],
[[0, 0], [1, 0], [1, 1], [0, 1], [0, 1, 0, 1]],
[[0, 0], [1, 0], [1, 1], [0, 0], [0, 1, 0, 1]],
[[0, 0], [1, 0], [1, 1], [1, 0], [0, 1, 0, 1]],
[[0, 0], [1, 0], [1, 1], [2, 0], [0, 2, 0, 1]],
[[0, 0], [1, 0], [0, 1], [1, 1], [0, 1, 0, 1]],
[[0, 0], [1, 0], [0, 1], [1, 2], [0, 1, 0, 2]],
[[0, 0], [1, 0], [0, 1], [0, 2], [0, 1, 0, 2]],
[[0, 0], [1, 0], [0, 1], [-1, 2], [-1, 1, 0, 2]],
[[0, 0], [1, 0], [0, 1], [-1, 1], [-1, 1, 0, 1]],
[[0, 0], [1, 0], [0, 1], [-1, 0], [-1, 1, 0, 1]],
[[0, 0], [1, 0], [0, 1], [0, 0], [0, 1, 0, 1]],
[[0, 0], [1, 0], [0, 1], [1, 0], [0, 1, 0, 1]],
[[0, 0], [1, 0], [0, 0], [1, 0], [0, 1, 0, 0]],
[[0, 0], [1, 0], [0, 0], [1, 1], [0, 1, 0, 1]],
[[0, 0], [1, 0], [0, 0], [0, 1], [0, 1, 0, 1]],
[[0, 0], [1, 0], [0, 0], [-1, 1], [-1, 1, 0, 1]],
[[0, 0], [1, 0], [0, 0], [-1, 0], [-1, 1, 0, 0]],
[[0, 0], [1, 0], [0, 0], [-1, -1], [-1, 1, -1, 0]],
[[0, 0], [1, 0], [0, 0], [0, -1], [0, 1, -1, 0]],
[[0, 0], [1, 0], [0, 0], [1, -1], [0, 1, -1, 0]],
[[0, 0], [1, 0], [0, -1], [1, -1], [0, 1, -1, 0]],
[[0, 0], [1, 0], [0, -1], [1, 0], [0, 1, -1, 0]],
[[0, 0], [1, 0], [0, -1], [0, 0], [0, 1, -1, 0]],
[[0, 0], [1, 0], [0, -1], [-1, 0], [-1, 1, -1, 0]],
[[0, 0], [1, 0], [0, -1], [-1, -1], [-1, 1, -1, 0]],
[[0, 0], [1, 0], [0, -1], [-1, -2], [-1, 1, -2, 0]],
[[0, 0], [1, 0], [0, -1], [0, -2], [0, 1, -2, 0]],
[[0, 0], [1, 0], [0, -1], [1, -2], [0, 1, -2, 0]],
[[0, 0], [1, 0], [1, -1], [2, -1], [0, 2, -1, 0]],
[[0, 0], [1, 0], [1, -1], [2, 0], [0, 2, -1, 0]],
[[0, 0], [1, 0], [1, -1], [1, 0], [0, 1, -1, 0]],
[[0, 0], [1, 0], [1, -1], [0, 0], [0, 1, -1, 0]],
[[0, 0], [1, 0], [1, -1], [0, -1], [0, 1, -1, 0]],
[[0, 0], [1, 0], [1, -1], [0, -2], [0, 1, -2, 0]],
[[0, 0], [1, 0], [1, -1], [1, -2], [0, 1, -2, 0]],
[[0, 0], [1, 0], [1, -1], [2, -2], [0, 2, -2, 0]],
[[0, 0], [1, 0], [2, -1], [3, -1], [0, 3, -1, 0]],
[[0, 0], [1, 0], [2, -1], [3, 0], [0, 3, -1, 0]],
[[0, 0], [1, 0], [2, -1], [2, 0], [0, 2, -1, 0]],
[[0, 0], [1, 0], [2, -1], [1, 0], [0, 2, -1, 0]],
[[0, 0], [1, 0], [2, -1], [1, -1], [0, 2, -1, 0]],
[[0, 0], [1, 0], [2, -1], [1, -2], [0, 2, -2, 0]],
[[0, 0], [1, 0], [2, -1], [2, -2], [0, 2, -2, 0]],
[[0, 0], [1, 0], [2, -1], [3, -2], [0, 3, -2, 0]],
[[0, 0], [1, 1], [2, 1], [3, 1], [0, 3, 0, 1]],
[[0, 0], [1, 1], [2, 1], [3, 2], [0, 3, 0, 2]],
[[0, 0], [1, 1], [2, 1], [2, 2], [0, 2, 0, 2]],
[[0, 0], [1, 1], [2, 1], [1, 2], [0, 2, 0, 2]],
[[0, 0], [1, 1], [2, 1], [1, 1], [0, 2, 0, 1]],
[[0, 0], [1, 1], [2, 1], [1, 0], [0, 2, 0, 1]],
[[0, 0], [1, 1], [2, 1], [2, 0], [0, 2, 0, 1]],
[[0, 0], [1, 1], [2, 1], [3, 0], [0, 3, 0, 1]],
[[0, 0], [1, 1], [2, 2], [3, 2], [0, 3, 0, 2]],
[[0, 0], [1, 1], [2, 2], [3, 3], [0, 3, 0, 3]],
[[0, 0], [1, 1], [2, 2], [2, 3], [0, 2, 0, 3]],
[[0, 0], [1, 1], [2, 2], [1, 3], [0, 2, 0, 3]],
[[0, 0], [1, 1], [2, 2], [1, 2], [0, 2, 0, 2]],
[[0, 0], [1, 1], [2, 2], [1, 1], [0, 2, 0, 2]],
[[0, 0], [1, 1], [2, 2], [2, 1], [0, 2, 0, 2]],
[[0, 0], [1, 1], [2, 2], [3, 1], [0, 3, 0, 2]],
[[0, 0], [1, 1], [1, 2], [2, 2], [0, 2, 0, 2]],
[[0, 0], [1, 1], [1, 2], [2, 3], [0, 2, 0, 3]],
[[0, 0], [1, 1], [1, 2], [1, 3], [0, 1, 0, 3]],
[[0, 0], [1, 1], [1, 2], [0, 3], [0, 1, 0, 3]],
[[0, 0], [1, 1], [1, 2], [0, 2], [0, 1, 0, 2]],
[[0, 0], [1, 1], [1, 2], [0, 1], [0, 1, 0, 2]],
[[0, 0], [1, 1], [1, 2], [1, 1], [0, 1, 0, 2]],
[[0, 0], [1, 1], [1, 2], [2, 1], [0, 2, 0, 2]],
[[0, 0], [1, 1], [0, 2], [1, 2], [0, 1, 0, 2]],
[[0, 0], [1, 1], [0, 2], [1, 3], [0, 1, 0, 3]],
[[0, 0], [1, 1], [0, 2], [0, 3], [0, 1, 0, 3]],
[[0, 0], [1, 1], [0, 2], [-1, 3], [-1, 1, 0, 3]],
[[0, 0], [1, 1], [0, 2], [-1, 2], [-1, 1, 0, 2]],
[[0, 0], [1, 1], [0, 2], [-1, 1], [-1, 1, 0, 2]],
[[0, 0], [1, 1], [0, 2], [0, 1], [0, 1, 0, 2]],
[[0, 0], [1, 1], [0, 2], [1, 1], [0, 1, 0, 2]],
[[0, 0], [1, 1], [0, 1], [1, 1], [0, 1, 0, 1]],
[[0, 0], [1, 1], [0, 1], [1, 2], [0, 1, 0, 2]],
[[0, 0], [1, 1], [0, 1], [0, 2], [0, 1, 0, 2]],
[[0, 0], [1, 1], [0, 1], [-1, 2], [-1, 1, 0, 2]],
[[0, 0], [1, 1], [0, 1], [-1, 1], [-1, 1, 0, 1]],
[[0, 0], [1, 1], [0, 1], [-1, 0], [-1, 1, 0, 1]],
[[0, 0], [1, 1], [0, 1], [0, 0], [0, 1, 0, 1]],
[[0, 0], [1, 1], [0, 1], [1, 0], [0, 1, 0, 1]],
[[0, 0], [1, 1], [0, 0], [1, 0], [0, 1, 0, 1]],
[[0, 0], [1, 1], [0, 0], [1, 1], [0, 1, 0, 1]],
[[0, 0], [1, 1], [0, 0], [0, 1], [0, 1, 0, 1]],
[[0, 0], [1, 1], [0, 0], [-1, 1], [-1, 1, 0, 1]],
[[0, 0], [1, 1], [0, 0], [-1, 0], [-1, 1, 0, 1]],
[[0, 0], [1, 1], [0, 0], [-1, -1], [-1, 1, -1, 1]],
[[0, 0], [1, 1], [0, 0], [0, -1], [0, 1, -1, 1]],
[[0, 0], [1, 1], [0, 0], [1, -1], [0, 1, -1, 1]],
[[0, 0], [1, 1], [1, 0], [2, 0], [0, 2, 0, 1]],
[[0, 0], [1, 1], [1, 0], [2, 1], [0, 2, 0, 1]],
[[0, 0], [1, 1], [1, 0], [1, 1], [0, 1, 0, 1]],
[[0, 0], [1, 1], [1, 0], [0, 1], [0, 1, 0, 1]],
[[0, 0], [1, 1], [1, 0], [0, 0], [0, 1, 0, 1]],
[[0, 0], [1, 1], [1, 0], [0, -1], [0, 1, -1, 1]],
[[0, 0], [1, 1], [1, 0], [1, -1], [0, 1, -1, 1]],
[[0, 0], [1, 1], [1, 0], [2, -1], [0, 2, -1, 1]],
[[0, 0], [1, 1], [2, 0], [3, 0], [0, 3, 0, 1]],
[[0, 0], [1, 1], [2, 0], [3, 1], [0, 3, 0, 1]],
[[0, 0], [1, 1], [2, 0], [2, 1], [0, 2, 0, 1]],
[[0, 0], [1, 1], [2, 0], [1, 1], [0, 2, 0, 1]],
[[0, 0], [1, 1], [2, 0], [1, 0], [0, 2, 0, 1]],
[[0, 0], [1, 1], [2, 0], [1, -1], [0, 2, -1, 1]],
[[0, 0], [1, 1], [2, 0], [2, -1], [0, 2, -1, 1]],
[[0, 0], [1, 1], [2, 0], [3, -1], [0, 3, -1, 1]],
[[0, 0], [0, 1], [1, 1], [2, 1], [0, 2, 0, 1]],
[[0, 0], [0, 1], [1, 1], [2, 2], [0, 2, 0, 2]],
[[0, 0], [0, 1], [1, 1], [1, 2], [0, 1, 0, 2]],
[[0, 0], [0, 1], [1, 1], [0, 2], [0, 1, 0, 2]],
[[0, 0], [0, 1], [1, 1], [0, 1], [0, 1, 0, 1]],
[[0, 0], [0, 1], [1, 1], [0, 0], [0, 1, 0, 1]],
[[0, 0], [0, 1], [1, 1], [1, 0], [0, 1, 0, 1]],
[[0, 0], [0, 1], [1, 1], [2, 0], [0, 2, 0, 1]],
[[0, 0], [0, 1], [1, 2], [2, 2], [0, 2, 0, 2]],
[[0, 0], [0, 1], [1, 2], [2, 3], [0, 2, 0, 3]],
[[0, 0], [0, 1], [1, 2], [1, 3], [0, 1, 0, 3]],
[[0, 0], [0, 1], [1, 2], [0, 3], [0, 1, 0, 3]],
[[0, 0], [0, 1], [1, 2], [0, 2], [0, 1, 0, 2]],
[[0, 0], [0, 1], [1, 2], [0, 1], [0, 1, 0, 2]],
[[0, 0], [0, 1], [1, 2], [1, 1], [0, 1, 0, 2]],
[[0, 0], [0, 1], [1, 2], [2, 1], [0, 2, 0, 2]],
[[0, 0], [0, 1], [0, 2], [1, 2], [0, 1, 0, 2]],
[[0, 0], [0, 1], [0, 2], [1, 3], [0, 1, 0, 3]],
[[0, 0], [0, 1], [0, 2], [0, 3], [0, 0, 0, 3]],
[[0, 0], [0, 1], [0, 2], [-1, 3], [-1, 0, 0, 3]],
[[0, 0], [0, 1], [0, 2], [-1, 2], [-1, 0, 0, 2]],
[[0, 0], [0, 1], [0, 2], [-1, 1], [-1, 0, 0, 2]],
[[0, 0], [0, 1], [0, 2], [0, 1], [0, 0, 0, 2]],
[[0, 0], [0, 1], [0, 2], [1, 1], [0, 1, 0, 2]],
[[0, 0], [0, 1], [-1, 2], [0, 2], [-1, 0, 0, 2]],
[[0, 0], [0, 1], [-1, 2], [0, 3], [-1, 0, 0, 3]],
[[0, 0], [0, 1], [-1, 2], [-1, 3], [-1, 0, 0, 3]],
[[0, 0], [0, 1], [-1, 2], [-2, 3], [-2, 0, 0, 3]],
[[0, 0], [0, 1], [-1, 2], [-2, 2], [-2, 0, 0, 2]],
[[0, 0], [0, 1], [-1, 2], [-2, 1], [-2, 0, 0, 2]],
[[0, 0], [0, 1], [-1, 2], [-1, 1], [-1, 0, 0, 2]],
[[0, 0], [0, 1], [-1, 2], [0, 1], [-1, 0, 0, 2]],
[[0, 0], [0, 1], [-1, 1], [0, 1], [-1, 0, 0, 1]],
[[0, 0], [0, 1], [-1, 1], [0, 2], [-1, 0, 0, 2]],
[[0, 0], [0, 1], [-1, 1], [-1, 2], [-1, 0, 0, 2]],
[[0, 0], [0, 1], [-1, 1], [-2, 2], [-2, 0, 0, 2]],
[[0, 0], [0, 1], [-1, 1], [-2, 1], [-2, 0, 0, 1]],
[[0, 0], [0, 1], [-1, 1], [-2, 0], [-2, 0, 0, 1]],
[[0, 0], [0, 1], [-1, 1], [-1, 0], [-1, 0, 0, 1]],
[[0, 0], [0, 1], [-1, 1], [0, 0], [-1, 0, 0, 1]],
[[0, 0], [0, 1], [-1, 0], [0, 0], [-1, 0, 0, 1]],
[[0, 0], [0, 1], [-1, 0], [0, 1], [-1, 0, 0, 1]],
[[0, 0], [0, 1], [-1, 0], [-1, 1], [-1, 0, 0, 1]],
[[0, 0], [0, 1], [-1, 0], [-2, 1], [-2, 0, 0, 1]],
[[0, 0], [0, 1], [-1, 0], [-2, 0], [-2, 0, 0, 1]],
[[0, 0], [0, 1], [-1, 0], [-2, -1], [-2, 0, -1, 1]],
[[0, 0], [0, 1], [-1, 0], [-1, -1], [-1, 0, -1, 1]],
[[0, 0], [0, 1], [-1, 0], [0, -1], [-1, 0, -1, 1]],
[[0, 0], [0, 1], [0, 0], [1, 0], [0, 1, 0, 1]],
[[0, 0], [0, 1], [0, 0], [1, 1], [0, 1, 0, 1]],
[[0, 0], [0, 1], [0, 0], [0, 1], [0, 0, 0, 1]],
[[0, 0], [0, 1], [0, 0], [-1, 1], [-1, 0, 0, 1]],
[[0, 0], [0, 1], [0, 0], [-1, 0], [-1, 0, 0, 1]],
[[0, 0], [0, 1], [0, 0], [-1, -1], [-1, 0, -1, 1]],
[[0, 0], [0, 1], [0, 0], [0, -1], [0, 0, -1, 1]],
[[0, 0], [0, 1], [0, 0], [1, -1], [0, 1, -1, 1]],
[[0, 0], [0, 1], [1, 0], [2, 0], [0, 2, 0, 1]],
[[0, 0], [0, 1], [1, 0], [2, 1], [0, 2, 0, 1]],
[[0, 0], [0, 1], [1, 0], [1, 1], [0, 1, 0, 1]],
[[0, 0], [0, 1], [1, 0], [0, 1], [0, 1, 0, 1]],
[[0, 0], [0, 1], [1, 0], [0, 0], [0, 1, 0, 1]],
[[0, 0], [0, 1], [1, 0], [0, -1], [0, 1, -1, 1]],
[[0, 0], [0, 1], [1, 0], [1, -1], [0, 1, -1, 1]],
[[0, 0], [0, 1], [1, 0], [2, -1], [0, 2, -1, 1]],
[[0, 0], [-1, 1], [0, 1], [1, 1], [-1, 1, 0, 1]],
[[0, 0], [-1, 1], [0, 1], [1, 2], [-1, 1, 0, 2]],
[[0, 0], [-1, 1], [0, 1], [0, 2], [-1, 0, 0, 2]],
[[0, 0], [-1, 1], [0, 1], [-1, 2], [-1, 0, 0, 2]],
[[0, 0], [-1, 1], [0, 1], [-1, 1], [-1, 0, 0, 1]],
[[0, 0], [-1, 1], [0, 1], [-1, 0], [-1, 0, 0, 1]],
[[0, 0], [-1, 1], [0, 1], [0, 0], [-1, 0, 0, 1]],
[[0, 0], [-1, 1], [0, 1], [1, 0], [-1, 1, 0, 1]],
[[0, 0], [-1, 1], [0, 2], [1, 2], [-1, 1, 0, 2]],
[[0, 0], [-1, 1], [0, 2], [1, 3], [-1, 1, 0, 3]],
[[0, 0], [-1, 1], [0, 2], [0, 3], [-1, 0, 0, 3]],
[[0, 0], [-1, 1], [0, 2], [-1, 3], [-1, 0, 0, 3]],
[[0, 0], [-1, 1], [0, 2], [-1, 2], [-1, 0, 0, 2]],
[[0, 0], [-1, 1], [0, 2], [-1, 1], [-1, 0, 0, 2]],
[[0, 0], [-1, 1], [0, 2], [0, 1], [-1, 0, 0, 2]],
[[0, 0], [-1, 1], [0, 2], [1, 1], [-1, 1, 0, 2]],
[[0, 0], [-1, 1], [-1, 2], [0, 2], [-1, 0, 0, 2]],
[[0, 0], [-1, 1], [-1, 2], [0, 3], [-1, 0, 0, 3]],
[[0, 0], [-1, 1], [-1, 2], [-1, 3], [-1, 0, 0, 3]],
[[0, 0], [-1, 1], [-1, 2], [-2, 3], [-2, 0, 0, 3]],
[[0, 0], [-1, 1], [-1, 2], [-2, 2], [-2, 0, 0, 2]],
[[0, 0], [-1, 1], [-1, 2], [-2, 1], [-2, 0, 0, 2]],
[[0, 0], [-1, 1], [-1, 2], [-1, 1], [-1, 0, 0, 2]],
[[0, 0], [-1, 1], [-1, 2], [0, 1], [-1, 0, 0, 2]],
[[0, 0], [-1, 1], [-2, 2], [-1, 2], [-2, 0, 0, 2]],
[[0, 0], [-1, 1], [-2, 2], [-1, 3], [-2, 0, 0, 3]],
[[0, 0], [-1, 1], [-2, 2], [-2, 3], [-2, 0, 0, 3]],
[[0, 0], [-1, 1], [-2, 2], [-3, 3], [-3, 0, 0, 3]],
[[0, 0], [-1, 1], [-2, 2], [-3, 2], [-3, 0, 0, 2]],
[[0, 0], [-1, 1], [-2, 2], [-3, 1], [-3, 0, 0, 2]],
[[0, 0], [-1, 1], [-2, 2], [-2, 1], [-2, 0, 0, 2]],
[[0, 0], [-1, 1], [-2, 2], [-1, 1], [-2, 0, 0, 2]],
[[0, 0], [-1, 1], [-2, 1], [-1, 1], [-2, 0, 0, 1]],
[[0, 0], [-1, 1], [-2, 1], [-1, 2], [-2, 0, 0, 2]],
[[0, 0], [-1, 1], [-2, 1], [-2, 2], [-2, 0, 0, 2]],
[[0, 0], [-1, 1], [-2, 1], [-3, 2], [-3, 0, 0, 2]],
[[0, 0], [-1, 1], [-2, 1], [-3, 1], [-3, 0, 0, 1]],
[[0, 0], [-1, 1], [-2, 1], [-3, 0], [-3, 0, 0, 1]],
[[0, 0], [-1, 1], [-2, 1], [-2, 0], [-2, 0, 0, 1]],
[[0, 0], [-1, 1], [-2, 1], [-1, 0], [-2, 0, 0, 1]],
[[0, 0], [-1, 1], [-2, 0], [-1, 0], [-2, 0, 0, 1]],
[[0, 0], [-1, 1], [-2, 0], [-1, 1], [-2, 0, 0, 1]],
[[0, 0], [-1, 1], [-2, 0], [-2, 1], [-2, 0, 0, 1]],
[[0, 0], [-1, 1], [-2, 0], [-3, 1], [-3, 0, 0, 1]],
[[0, 0], [-1, 1], [-2, 0], [-3, 0], [-3, 0, 0, 1]],
[[0, 0], [-1, 1], [-2, 0], [-3, -1], [-3, 0, -1, 1]],
[[0, 0], [-1, 1], [-2, 0], [-2, -1], [-2, 0, -1, 1]],
[[0, 0], [-1, 1], [-2, 0], [-1, -1], [-2, 0, -1, 1]],
[[0, 0], [-1, 1], [-1, 0], [0, 0], [-1, 0, 0, 1]],
[[0, 0], [-1, 1], [-1, 0], [0, 1], [-1, 0, 0, 1]],
[[0, 0], [-1, 1], [-1, 0], [-1, 1], [-1, 0, 0, 1]],
[[0, 0], [-1, 1], [-1, 0], [-2, 1], [-2, 0, 0, 1]],
[[0, 0], [-1, 1], [-1, 0], [-2, 0], [-2, 0, 0, 1]],
[[0, 0], [-1, 1], [-1, 0], [-2, -1], [-2, 0, -1, 1]],
[[0, 0], [-1, 1], [-1, 0], [-1, -1], [-1, 0, -1, 1]],
[[0, 0], [-1, 1], [-1, 0], [0, -1], [-1, 0, -1, 1]],
[[0, 0], [-1, 1], [0, 0], [1, 0], [-1, 1, 0, 1]],
[[0, 0], [-1, 1], [0, 0], [1, 1], [-1, 1, 0, 1]],
[[0, 0], [-1, 1], [0, 0], [0, 1], [-1, 0, 0, 1]],
[[0, 0], [-1, 1], [0, 0], [-1, 1], [-1, 0, 0, 1]],
[[0, 0], [-1, 1], [0, 0], [-1, 0], [-1, 0, 0, 1]],
[[0, 0], [-1, 1], [0, 0], [-1, -1], [-1, 0, -1, 1]],
[[0, 0], [-1, 1], [0, 0], [0, -1], [-1, 0, -1, 1]],
[[0, 0], [-1, 1], [0, 0], [1, -1], [-1, 1, -1, 1]],
[[0, 0], [-1, 0], [0, 0], [1, 0], [-1, 1, 0, 0]],
[[0, 0], [-1, 0], [0, 0], [1, 1], [-1, 1, 0, 1]],
[[0, 0], [-1, 0], [0, 0], [0, 1], [-1, 0, 0, 1]],
[[0, 0], [-1, 0], [0, 0], [-1, 1], [-1, 0, 0, 1]],
[[0, 0], [-1, 0], [0, 0], [-1, 0], [-1, 0, 0, 0]],
[[0, 0], [-1, 0], [0, 0], [-1, -1], [-1, 0, -1, 0]],
[[0, 0], [-1, 0], [0, 0], [0, -1], [-1, 0, -1, 0]],
[[0, 0], [-1, 0], [0, 0], [1, -1], [-1, 1, -1, 0]],
[[0, 0], [-1, 0], [0, 1], [1, 1], [-1, 1, 0, 1]],
[[0, 0], [-1, 0], [0, 1], [1, 2], [-1, 1, 0, 2]],
[[0, 0], [-1, 0], [0, 1], [0, 2], [-1, 0, 0, 2]],
[[0, 0], [-1, 0], [0, 1], [-1, 2], [-1, 0, 0, 2]],
[[0, 0], [-1, 0], [0, 1], [-1, 1], [-1, 0, 0, 1]],
[[0, 0], [-1, 0], [0, 1], [-1, 0], [-1, 0, 0, 1]],
[[0, 0], [-1, 0], [0, 1], [0, 0], [-1, 0, 0, 1]],
[[0, 0], [-1, 0], [0, 1], [1, 0], [-1, 1, 0, 1]],
[[0, 0], [-1, 0], [-1, 1], [0, 1], [-1, 0, 0, 1]],
[[0, 0], [-1, 0], [-1, 1], [0, 2], [-1, 0, 0, 2]],
[[0, 0], [-1, 0], [-1, 1], [-1, 2], [-1, 0, 0, 2]],
[[0, 0], [-1, 0], [-1, 1], [-2, 2], [-2, 0, 0, 2]],
[[0, 0], [-1, 0], [-1, 1], [-2, 1], [-2, 0, 0, 1]],
[[0, 0], [-1, 0], [-1, 1], [-2, 0], [-2, 0, 0, 1]],
[[0, 0], [-1, 0], [-1, 1], [-1, 0], [-1, 0, 0, 1]],
[[0, 0], [-1, 0], [-1, 1], [0, 0], [-1, 0, 0, 1]],
[[0, 0], [-1, 0], [-2, 1], [-1, 1], [-2, 0, 0, 1]],
[[0, 0], [-1, 0], [-2, 1], [-1, 2], [-2, 0, 0, 2]],
[[0, 0], [-1, 0], [-2, 1], [-2, 2], [-2, 0, 0, 2]],
[[0, 0], [-1, 0], [-2, 1], [-3, 2], [-3, 0, 0, 2]],
[[0, 0], [-1, 0], [-2, 1], [-3, 1], [-3, 0, 0, 1]],
[[0, 0], [-1, 0], [-2, 1], [-3, 0], [-3, 0, 0, 1]],
[[0, 0], [-1, 0], [-2, 1], [-2, 0], [-2, 0, 0, 1]],
[[0, 0], [-1, 0], [-2, 1], [-1, 0], [-2, 0, 0, 1]],
[[0, 0], [-1, 0], [-2, 0], [-1, 0], [-2, 0, 0, 0]],
[[0, 0], [-1, 0], [-2, 0], [-1, 1], [-2, 0, 0, 1]],
[[0, 0], [-1, 0], [-2, 0], [-2, 1], [-2, 0, 0, 1]],
[[0, 0], [-1, 0], [-2, 0], [-3, 1], [-3, 0, 0, 1]],
[[0, 0], [-1, 0], [-2, 0], [-3, 0], [-3, 0, 0, 0]],
[[0, 0], [-1, 0], [-2, 0], [-3, -1], [-3, 0, -1, 0]],
[[0, 0], [-1, 0], [-2, 0], [-2, -1], [-2, 0, -1, 0]],
[[0, 0], [-1, 0], [-2, 0], [-1, -1], [-2, 0, -1, 0]],
[[0, 0], [-1, 0], [-2, -1], [-1, -1], [-2, 0, -1, 0]],
[[0, 0], [-1, 0], [-2, -1], [-1, 0], [-2, 0, -1, 0]],
[[0, 0], [-1, 0], [-2, -1], [-2, 0], [-2, 0, -1, 0]],
[[0, 0], [-1, 0], [-2, -1], [-3, 0], [-3, 0, -1, 0]],
[[0, 0], [-1, 0], [-2, -1], [-3, -1], [-3, 0, -1, 0]],
[[0, 0], [-1, 0], [-2, -1], [-3, -2], [-3, 0, -2, 0]],
[[0, 0], [-1, 0], [-2, -1], [-2, -2], [-2, 0, -2, 0]],
[[0, 0], [-1, 0], [-2, -1], [-1, -2], [-2, 0, -2, 0]],
[[0, 0], [-1, 0], [-1, -1], [0, -1], [-1, 0, -1, 0]],
[[0, 0], [-1, 0], [-1, -1], [0, 0], [-1, 0, -1, 0]],
[[0, 0], [-1, 0], [-1, -1], [-1, 0], [-1, 0, -1, 0]],
[[0, 0], [-1, 0], [-1, -1], [-2, 0], [-2, 0, -1, 0]],
[[0, 0], [-1, 0], [-1, -1], [-2, -1], [-2, 0, -1, 0]],
[[0, 0], [-1, 0], [-1, -1], [-2, -2], [-2, 0, -2, 0]],
[[0, 0], [-1, 0], [-1, -1], [-1, -2], [-1, 0, -2, 0]],
[[0, 0], [-1, 0], [-1, -1], [0, -2], [-1, 0, -2, 0]],
[[0, 0], [-1, 0], [0, -1], [1, -1], [-1, 1, -1, 0]],
[[0, 0], [-1, 0], [0, -1], [1, 0], [-1, 1, -1, 0]],
[[0, 0], [-1, 0], [0, -1], [0, 0], [-1, 0, -1, 0]],
[[0, 0], [-1, 0], [0, -1], [-1, 0], [-1, 0, -1, 0]],
[[0, 0], [-1, 0], [0, -1], [-1, -1], [-1, 0, -1, 0]],
[[0, 0], [-1, 0], [0, -1], [-1, -2], [-1, 0, -2, 0]],
[[0, 0], [-1, 0], [0, -1], [0, -2], [-1, 0, -2, 0]],
[[0, 0], [-1, 0], [0, -1], [1, -2], [-1, 1, -2, 0]],
[[0, 0], [-1, -1], [0, -1], [1, -1], [-1, 1, -1, 0]],
[[0, 0], [-1, -1], [0, -1], [1, 0], [-1, 1, -1, 0]],
[[0, 0], [-1, -1], [0, -1], [0, 0], [-1, 0, -1, 0]],
[[0, 0], [-1, -1], [0, -1], [-1, 0], [-1, 0, -1, 0]],
[[0, 0], [-1, -1], [0, -1], [-1, -1], [-1, 0, -1, 0]],
[[0, 0], [-1, -1], [0, -1], [-1, -2], [-1, 0, -2, 0]],
[[0, 0], [-1, -1], [0, -1], [0, -2], [-1, 0, -2, 0]],
[[0, 0], [-1, -1], [0, -1], [1, -2], [-1, 1, -2, 0]],
[[0, 0], [-1, -1], [0, 0], [1, 0], [-1, 1, -1, 0]],
[[0, 0], [-1, -1], [0, 0], [1, 1], [-1, 1, -1, 1]],
[[0, 0], [-1, -1], [0, 0], [0, 1], [-1, 0, -1, 1]],
[[0, 0], [-1, -1], [0, 0], [-1, 1], [-1, 0, -1, 1]],
[[0, 0], [-1, -1], [0, 0], [-1, 0], [-1, 0, -1, 0]],
[[0, 0], [-1, -1], [0, 0], [-1, -1], [-1, 0, -1, 0]],
[[0, 0], [-1, -1], [0, 0], [0, -1], [-1, 0, -1, 0]],
[[0, 0], [-1, -1], [0, 0], [1, -1], [-1, 1, -1, 0]],
[[0, 0], [-1, -1], [-1, 0], [0, 0], [-1, 0, -1, 0]],
[[0, 0], [-1, -1], [-1, 0], [0, 1], [-1, 0, -1, 1]],
[[0, 0], [-1, -1], [-1, 0], [-1, 1], [-1, 0, -1, 1]],
[[0, 0], [-1, -1], [-1, 0], [-2, 1], [-2, 0, -1, 1]],
[[0, 0], [-1, -1], [-1, 0], [-2, 0], [-2, 0, -1, 0]],
[[0, 0], [-1, -1], [-1, 0], [-2, -1], [-2, 0, -1, 0]],
[[0, 0], [-1, -1], [-1, 0], [-1, -1], [-1, 0, -1, 0]],
[[0, 0], [-1, -1], [-1, 0], [0, -1], [-1, 0, -1, 0]],
[[0, 0], [-1, -1], [-2, 0], [-1, 0], [-2, 0, -1, 0]],
[[0, 0], [-1, -1], [-2, 0], [-1, 1], [-2, 0, -1, 1]],
[[0, 0], [-1, -1], [-2, 0], [-2, 1], [-2, 0, -1, 1]],
[[0, 0], [-1, -1], [-2, 0], [-3, 1], [-3, 0, -1, 1]],
[[0, 0], [-1, -1], [-2, 0], [-3, 0], [-3, 0, -1, 0]],
[[0, 0], [-1, -1], [-2, 0], [-3, -1], [-3, 0, -1, 0]],
[[0, 0], [-1, -1], [-2, 0], [-2, -1], [-2, 0, -1, 0]],
[[0, 0], [-1, -1], [-2, 0], [-1, -1], [-2, 0, -1, 0]],
[[0, 0], [-1, -1], [-2, -1], [-1, -1], [-2, 0, -1, 0]],
[[0, 0], [-1, -1], [-2, -1], [-1, 0], [-2, 0, -1, 0]],
[[0, 0], [-1, -1], [-2, -1], [-2, 0], [-2, 0, -1, 0]],
[[0, 0], [-1, -1], [-2, -1], [-3, 0], [-3, 0, -1, 0]],
[[0, 0], [-1, -1], [-2, -1], [-3, -1], [-3, 0, -1, 0]],
[[0, 0], [-1, -1], [-2, -1], [-3, -2], [-3, 0, -2, 0]],
[[0, 0], [-1, -1], [-2, -1], [-2, -2], [-2, 0, -2, 0]],
[[0, 0], [-1, -1], [-2, -1], [-1, -2], [-2, 0, -2, 0]],
[[0, 0], [-1, -1], [-2, -2], [-1, -2], [-2, 0, -2, 0]],
[[0, 0], [-1, -1], [-2, -2], [-1, -1], [-2, 0, -2, 0]],
[[0, 0], [-1, -1], [-2, -2], [-2, -1], [-2, 0, -2, 0]],
[[0, 0], [-1, -1], [-2, -2], [-3, -1], [-3, 0, -2, 0]],
[[0, 0], [-1, -1], [-2, -2], [-3, -2], [-3, 0, -2, 0]],
[[0, 0], [-1, -1], [-2, -2], [-3, -3], [-3, 0, -3, 0]],
[[0, 0], [-1, -1], [-2, -2], [-2, -3], [-2, 0, -3, 0]],
[[0, 0], [-1, -1], [-2, -2], [-1, -3], [-2, 0, -3, 0]],
[[0, 0], [-1, -1], [-1, -2], [0, -2], [-1, 0, -2, 0]],
[[0, 0], [-1, -1], [-1, -2], [0, -1], [-1, 0, -2, 0]],
[[0, 0], [-1, -1], [-1, -2], [-1, -1], [-1, 0, -2, 0]],
[[0, 0], [-1, -1], [-1, -2], [-2, -1], [-2, 0, -2, 0]],
[[0, 0], [-1, -1], [-1, -2], [-2, -2], [-2, 0, -2, 0]],
[[0, 0], [-1, -1], [-1, -2], [-2, -3], [-2, 0, -3, 0]],
[[0, 0], [-1, -1], [-1, -2], [-1, -3], [-1, 0, -3, 0]],
[[0, 0], [-1, -1], [-1, -2], [0, -3], [-1, 0, -3, 0]],
[[0, 0], [-1, -1], [0, -2], [1, -2], [-1, 1, -2, 0]],
[[0, 0], [-1, -1], [0, -2], [1, -1], [-1, 1, -2, 0]],
[[0, 0], [-1, -1], [0, -2], [0, -1], [-1, 0, -2, 0]],
[[0, 0], [-1, -1], [0, -2], [-1, -1], [-1, 0, -2, 0]],
[[0, 0], [-1, -1], [0, -2], [-1, -2], [-1, 0, -2, 0]],
[[0, 0], [-1, -1], [0, -2], [-1, -3], [-1, 0, -3, 0]],
[[0, 0], [-1, -1], [0, -2], [0, -3], [-1, 0, -3, 0]],
[[0, 0], [-1, -1], [0, -2], [1, -3], [-1, 1, -3, 0]],
[[0, 0], [0, -1], [1, -1], [2, -1], [0, 2, -1, 0]],
[[0, 0], [0, -1], [1, -1], [2, 0], [0, 2, -1, 0]],
[[0, 0], [0, -1], [1, -1], [1, 0], [0, 1, -1, 0]],
[[0, 0], [0, -1], [1, -1], [0, 0], [0, 1, -1, 0]],
[[0, 0], [0, -1], [1, -1], [0, -1], [0, 1, -1, 0]],
[[0, 0], [0, -1], [1, -1], [0, -2], [0, 1, -2, 0]],
[[0, 0], [0, -1], [1, -1], [1, -2], [0, 1, -2, 0]],
[[0, 0], [0, -1], [1, -1], [2, -2], [0, 2, -2, 0]],
[[0, 0], [0, -1], [1, 0], [2, 0], [0, 2, -1, 0]],
[[0, 0], [0, -1], [1, 0], [2, 1], [0, 2, -1, 1]],
[[0, 0], [0, -1], [1, 0], [1, 1], [0, 1, -1, 1]],
[[0, 0], [0, -1], [1, 0], [0, 1], [0, 1, -1, 1]],
[[0, 0], [0, -1], [1, 0], [0, 0], [0, 1, -1, 0]],
[[0, 0], [0, -1], [1, 0], [0, -1], [0, 1, -1, 0]],
[[0, 0], [0, -1], [1, 0], [1, -1], [0, 1, -1, 0]],
[[0, 0], [0, -1], [1, 0], [2, -1], [0, 2, -1, 0]],
[[0, 0], [0, -1], [0, 0], [1, 0], [0, 1, -1, 0]],
[[0, 0], [0, -1], [0, 0], [1, 1], [0, 1, -1, 1]],
[[0, 0], [0, -1], [0, 0], [0, 1], [0, 0, -1, 1]],
[[0, 0], [0, -1], [0, 0], [-1, 1], [-1, 0, -1, 1]],
[[0, 0], [0, -1], [0, 0], [-1, 0], [-1, 0, -1, 0]],
[[0, 0], [0, -1], [0, 0], [-1, -1], [-1, 0, -1, 0]],
[[0, 0], [0, -1], [0, 0], [0, -1], [0, 0, -1, 0]],
[[0, 0], [0, -1], [0, 0], [1, -1], [0, 1, -1, 0]],
[[0, 0], [0, -1], [-1, 0], [0, 0], [-1, 0, -1, 0]],
[[0, 0], [0, -1], [-1, 0], [0, 1], [-1, 0, -1, 1]],
[[0, 0], [0, -1], [-1, 0], [-1, 1], [-1, 0, -1, 1]],
[[0, 0], [0, -1], [-1, 0], [-2, 1], [-2, 0, -1, 1]],
[[0, 0], [0, -1], [-1, 0], [-2, 0], [-2, 0, -1, 0]],
[[0, 0], [0, -1], [-1, 0], [-2, -1], [-2, 0, -1, 0]],
[[0, 0], [0, -1], [-1, 0], [-1, -1], [-1, 0, -1, 0]],
[[0, 0], [0, -1], [-1, 0], [0, -1], [-1, 0, -1, 0]],
[[0, 0], [0, -1], [-1, -1], [0, -1], [-1, 0, -1, 0]],
[[0, 0], [0, -1], [-1, -1], [0, 0], [-1, 0, -1, 0]],
[[0, 0], [0, -1], [-1, -1], [-1, 0], [-1, 0, -1, 0]],
[[0, 0], [0, -1], [-1, -1], [-2, 0], [-2, 0, -1, 0]],
[[0, 0], [0, -1], [-1, -1], [-2, -1], [-2, 0, -1, 0]],
[[0, 0], [0, -1], [-1, -1], [-2, -2], [-2, 0, -2, 0]],
[[0, 0], [0, -1], [-1, -1], [-1, -2], [-1, 0, -2, 0]],
[[0, 0], [0, -1], [-1, -1], [0, -2], [-1, 0, -2, 0]],
[[0, 0], [0, -1], [-1, -2], [0, -2], [-1, 0, -2, 0]],
[[0, 0], [0, -1], [-1, -2], [0, -1], [-1, 0, -2, 0]],
[[0, 0], [0, -1], [-1, -2], [-1, -1], [-1, 0, -2, 0]],
[[0, 0], [0, -1], [-1, -2], [-2, -1], [-2, 0, -2, 0]],
[[0, 0], [0, -1], [-1, -2], [-2, -2], [-2, 0, -2, 0]],
[[0, 0], [0, -1], [-1, -2], [-2, -3], [-2, 0, -3, 0]],
[[0, 0], [0, -1], [-1, -2], [-1, -3], [-1, 0, -3, 0]],
[[0, 0], [0, -1], [-1, -2], [0, -3], [-1, 0, -3, 0]],
[[0, 0], [0, -1], [0, -2], [1, -2], [0, 1, -2, 0]],
[[0, 0], [0, -1], [0, -2], [1, -1], [0, 1, -2, 0]],
[[0, 0], [0, -1], [0, -2], [0, -1], [0, 0, -2, 0]],
[[0, 0], [0, -1], [0, -2], [-1, -1], [-1, 0, -2, 0]],
[[0, 0], [0, -1], [0, -2], [-1, -2], [-1, 0, -2, 0]],
[[0, 0], [0, -1], [0, -2], [-1, -3], [-1, 0, -3, 0]],
[[0, 0], [0, -1], [0, -2], [0, -3], [0, 0, -3, 0]],
[[0, 0], [0, -1], [0, -2], [1, -3], [0, 1, -3, 0]],
[[0, 0], [0, -1], [1, -2], [2, -2], [0, 2, -2, 0]],
[[0, 0], [0, -1], [1, -2], [2, -1], [0, 2, -2, 0]],
[[0, 0], [0, -1], [1, -2], [1, -1], [0, 1, -2, 0]],
[[0, 0], [0, -1], [1, -2], [0, -1], [0, 1, -2, 0]],
[[0, 0], [0, -1], [1, -2], [0, -2], [0, 1, -2, 0]],
[[0, 0], [0, -1], [1, -2], [0, -3], [0, 1, -3, 0]],
[[0, 0], [0, -1], [1, -2], [1, -3], [0, 1, -3, 0]],
[[0, 0], [0, -1], [1, -2], [2, -3], [0, 2, -3, 0]],
[[0, 0], [1, -1], [2, -1], [3, -1], [0, 3, -1, 0]],
[[0, 0], [1, -1], [2, -1], [3, 0], [0, 3, -1, 0]],
[[0, 0], [1, -1], [2, -1], [2, 0], [0, 2, -1, 0]],
[[0, 0], [1, -1], [2, -1], [1, 0], [0, 2, -1, 0]],
[[0, 0], [1, -1], [2, -1], [1, -1], [0, 2, -1, 0]],
[[0, 0], [1, -1], [2, -1], [1, -2], [0, 2, -2, 0]],
[[0, 0], [1, -1], [2, -1], [2, -2], [0, 2, -2, 0]],
[[0, 0], [1, -1], [2, -1], [3, -2], [0, 3, -2, 0]],
[[0, 0], [1, -1], [2, 0], [3, 0], [0, 3, -1, 0]],
[[0, 0], [1, -1], [2, 0], [3, 1], [0, 3, -1, 1]],
[[0, 0], [1, -1], [2, 0], [2, 1], [0, 2, -1, 1]],
[[0, 0], [1, -1], [2, 0], [1, 1], [0, 2, -1, 1]],
[[0, 0], [1, -1], [2, 0], [1, 0], [0, 2, -1, 0]],
[[0, 0], [1, -1], [2, 0], [1, -1], [0, 2, -1, 0]],
[[0, 0], [1, -1], [2, 0], [2, -1], [0, 2, -1, 0]],
[[0, 0], [1, -1], [2, 0], [3, -1], [0, 3, -1, 0]],
[[0, 0], [1, -1], [1, 0], [2, 0], [0, 2, -1, 0]],
[[0, 0], [1, -1], [1, 0], [2, 1], [0, 2, -1, 1]],
[[0, 0], [1, -1], [1, 0], [1, 1], [0, 1, -1, 1]],
[[0, 0], [1, -1], [1, 0], [0, 1], [0, 1, -1, 1]],
[[0, 0], [1, -1], [1, 0], [0, 0], [0, 1, -1, 0]],
[[0, 0], [1, -1], [1, 0], [0, -1], [0, 1, -1, 0]],
[[0, 0], [1, -1], [1, 0], [1, -1], [0, 1, -1, 0]],
[[0, 0], [1, -1], [1, 0], [2, -1], [0, 2, -1, 0]],
[[0, 0], [1, -1], [0, 0], [1, 0], [0, 1, -1, 0]],
[[0, 0], [1, -1], [0, 0], [1, 1], [0, 1, -1, 1]],
[[0, 0], [1, -1], [0, 0], [0, 1], [0, 1, -1, 1]],
[[0, 0], [1, -1], [0, 0], [-1, 1], [-1, 1, -1, 1]],
[[0, 0], [1, -1], [0, 0], [-1, 0], [-1, 1, -1, 0]],
[[0, 0], [1, -1], [0, 0], [-1, -1], [-1, 1, -1, 0]],
[[0, 0], [1, -1], [0, 0], [0, -1], [0, 1, -1, 0]],
[[0, 0], [1, -1], [0, 0], [1, -1], [0, 1, -1, 0]],
[[0, 0], [1, -1], [0, -1], [1, -1], [0, 1, -1, 0]],
[[0, 0], [1, -1], [0, -1], [1, 0], [0, 1, -1, 0]],
[[0, 0], [1, -1], [0, -1], [0, 0], [0, 1, -1, 0]],
[[0, 0], [1, -1], [0, -1], [-1, 0], [-1, 1, -1, 0]],
[[0, 0], [1, -1], [0, -1], [-1, -1], [-1, 1, -1, 0]],
[[0, 0], [1, -1], [0, -1], [-1, -2], [-1, 1, -2, 0]],
[[0, 0], [1, -1], [0, -1], [0, -2], [0, 1, -2, 0]],
[[0, 0], [1, -1], [0, -1], [1, -2], [0, 1, -2, 0]],
[[0, 0], [1, -1], [0, -2], [1, -2], [0, 1, -2, 0]],
[[0, 0], [1, -1], [0, -2], [1, -1], [0, 1, -2, 0]],
[[0, 0], [1, -1], [0, -2], [0, -1], [0, 1, -2, 0]],
[[0, 0], [1, -1], [0, -2], [-1, -1], [-1, 1, -2, 0]],
[[0, 0], [1, -1], [0, -2], [-1, -2], [-1, 1, -2, 0]],
[[0, 0], [1, -1], [0, -2], [-1, -3], [-1, 1, -3, 0]],
[[0, 0], [1, -1], [0, -2], [0, -3], [0, 1, -3, 0]],
[[0, 0], [1, -1], [0, -2], [1, -3], [0, 1, -3, 0]],
[[0, 0], [1, -1], [1, -2], [2, -2], [0, 2, -2, 0]],
[[0, 0], [1, -1], [1, -2], [2, -1], [0, 2, -2, 0]],
[[0, 0], [1, -1], [1, -2], [1, -1], [0, 1, -2, 0]],
[[0, 0], [1, -1], [1, -2], [0, -1], [0, 1, -2, 0]],
[[0, 0], [1, -1], [1, -2], [0, -2], [0, 1, -2, 0]],
[[0, 0], [1, -1], [1, -2], [0, -3], [0, 1, -3, 0]],
[[0, 0], [1, -1], [1, -2], [1, -3], [0, 1, -3, 0]],
[[0, 0], [1, -1], [1, -2], [2, -3], [0, 2, -3, 0]],
[[0, 0], [1, -1], [2, -2], [3, -2], [0, 3, -2, 0]],
[[0, 0], [1, -1], [2, -2], [3, -1], [0, 3, -2, 0]],
[[0, 0], [1, -1], [2, -2], [2, -1], [0, 2, -2, 0]],
[[0, 0], [1, -1], [2, -2], [1, -1], [0, 2, -2, 0]],
[[0, 0], [1, -1], [2, -2], [1, -2], [0, 2, -2, 0]],
[[0, 0], [1, -1], [2, -2], [1, -3], [0, 2, -3, 0]],
[[0, 0], [1, -1], [2, -2], [2, -3], [0, 2, -3, 0]],
[[0, 0], [1, -1], [2, -2], [3, -3], [0, 3, -3, 0]]]
cease=False
while cease==False:
    G=0
    l=[]
    for i in range(8):
        rr=[]
        for j in range(14):
            rr.append(str(random.randrange(0,10)))
        l.append(rr)
    
    while 1:
        W=[]
        d={}
        WW=[]
        for X in range(8):
            print(f'scanning X = {X}...')
            for Y in range(14):
                for Z in range(10):
                    L=[]
                    for uu in l:
                        L.append(uu[:])
                    L[X][Y]=str(Z)
                    e=[]
                    for r in range(8):
                        for c in range(14):
                            for i in R:
                                rmin,rmax,cmin,cmax=i[-1]
                                if 0<=r+rmin and r+rmax<8 and 0<=c+cmin and c+cmax<14:
                                    f=''
                                    for F in range(len(i)-1):
                                        f+=str(L[r+i[F][0]][c+i[F][1]])
                                    e.append(int(f))
                    o=list(sorted(set(e)))
                    g=-1
                    while o[g+1]==g+1:
                        g+=1
                    W.append(g)
                    M=max(W)
                    if g==G and l[X][Y]!=str(Z):
                        WW.append([X,Y,Z])
                    d[g]=[X,Y,Z]
        M=max(W)
        if M>G:
            G=M
            X,Y,Z=d[M]
            l[X][Y]=str(Z)
            print('\n')
            for i in l:
                print(''.join(i))
            print(M)
            print('\n')
            if 8140<=M:
                cease=True
                break
        else:
            print('')
            print('no progress')
            tt=len(WW)
            print(f'len(WW) = {tt}')
            b=-1
            while b<len(WW)-1:
                b+=1
                X,Y,Z=WW[b]
                print('')
                print(f'trying {X}, {Y}, {Z} : ({b+1}/{tt})\n')
                L=[]
                for uu in l:
                    L.append(uu[:])
                L[X][Y]=str(Z)
                while 1:
                    W=[]
                    d={}
                    for X in range(8):
                        print(f'scanning X = {X}...')
                        for Y in range(14):
                            for Z in range(10):
                                LL=[]
                                for uu in L:
                                    LL.append(uu[:])
                                LL[X][Y]=str(Z)
                                e=[]
                                for r in range(8):
                                    for c in range(14):
                                        for i in R:
                                            rmin,rmax,cmin,cmax=i[-1]
                                            if 0<=r+rmin and r+rmax<8 and 0<=c+cmin and c+cmax<14:
                                                f=''
                                                for F in range(len(i)-1):
                                                    f+=str(LL[r+i[F][0]][c+i[F][1]])
                                                e.append(int(f))
                                o=list(sorted(set(e)))
                                g=-1
                                while o[g+1]==g+1:
                                    g+=1
                                W.append(g)
                                M=max(W)
                                d[g]=[X,Y,Z]
                    M=max(W)
                    if M>G:
                        G=M
                        X,Y,Z=d[M]
                        l[X][Y]=str(Z)
                        print('\n')
                        for i in l:
                            print(''.join(i))
                        print(M)
                        print('\n')
                        if 8140<=M:
                            cease=True
                            b=9**9
                            break
                    else:
                        print(M)
                        break
            M=max(W) if W!=[] else -1
            if M>G:
                continue
                G=M
                X,Y,Z=dd[M]
                l[X][Y]=str(Z)
                print('\n')
                for i in l:
                    print(''.join(i))
                print(M)
                print('\n')
                if 8140<=M:
                    cease=True
                    break
            else:
                print('/nreset!/n')
                break
