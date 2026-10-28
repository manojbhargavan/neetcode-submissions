from typing import List


def find_max_in_each_list(nested_arr: List[List[int]]) -> List[int]:
    maxs = []
    for subl in nested_arr:
        max_current = subl[0]
        for item in subl:
            if max_current < item:
                max_current = item
        maxs.append(max_current)
    return maxs


# do not modify below this line
print(find_max_in_each_list([[1, 2], [3, 4, 2]]))
print(find_max_in_each_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(find_max_in_each_list([[5, 6, 2, 8], [9], [9, 10], [11, 10, 11]]))
