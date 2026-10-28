from typing import List


def get_index_of_seven(nums: List[int]) -> int:
    for index, num in enumerate(nums):
        if num == 7:
            return index
    return -1


def get_dist_between_sevens(nums: List[int]) -> int:
    first_7 = -1
    second_7 = -1
    found = 0
    for index, num in enumerate(nums):
        if num == 7:
            if found == 0:
                first_7 = index
                found += 1
            else:
                second_7 = index
                found += 2
                break
    return second_7 - first_7


# do not modify below this line
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 8, 9]))
print(get_index_of_seven([2, 4, 7, 5, 7, 8, 4, 2]))

print(get_dist_between_sevens([1, 2, 7, 4, 5, 6, 7, 8, 9]))
print(get_dist_between_sevens([2, 7, 7, 7, 8]))
print(get_dist_between_sevens([7, 4, 8, 4, 2, 7]))
