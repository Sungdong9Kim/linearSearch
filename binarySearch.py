def binary_search(element, some_list):
# 코드를 작성하세요.
    if element == some_list[len(some_list)//2]:
        return len(some_list) // 2
    elif element < some_list[len(some_list)//2]:
        

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))