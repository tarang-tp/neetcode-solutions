from typing import List

def read_integers() -> List[int]:
    string = input().split(",")
    num = []
    for i in string:
        num.append(int(i))
    return num
# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
