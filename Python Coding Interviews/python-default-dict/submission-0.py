from collections import defaultdict
from typing import List, Dict

def count_chars(s: str) -> Dict[str, int]:
    result = defaultdict(int)
    for c in s:
        if c in result:
            result[c] = result[c] + 1
        else:
            result[c] = 1
    return result

def nested_list_to_dict(nums: List[List[int]]) -> Dict[int, List[int]]:
    result = defaultdict(list)
    for r in nums:
        if r[0] in result:
            result[r[0]].extend(r[1:])
        else:
            result[r[0]] = r[1:]
    return result

# do not modify below this line
print(count_chars("hello"))
print(count_chars("helloworld"))
print(count_chars("areallylongstringwhyareyoureadingthishahalol"))

print(nested_list_to_dict([[1, 2, 3], [4, 5, 6], [1, 4]]))
print(nested_list_to_dict([[1, 2, 3, 4], [4, 5, 6, 7], [1, 4, 5, 6]]))
print(nested_list_to_dict([[5, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]))
print(nested_list_to_dict([[3, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8]]))
