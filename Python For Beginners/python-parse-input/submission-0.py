from typing import List

def read_integers() -> List[int]:
    result = []
    input_str = input()
    for n in input_str.split(","):
        result.append(int(n))
    return result

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
