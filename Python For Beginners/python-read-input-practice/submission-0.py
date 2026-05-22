def add_two_numbers() -> int:
    string = input().split(",")
    num = []
    for i in string:
        num.append(int(i))
    return sum(num)



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
