def binary_search(element, some_list):
# 코드를 작성하세요.
    minIndex = 0;
    maxIndex = len(some_list)
    for i in range(0, len(some_list)):
        if element == some_list[(minIndex + maxIndex)//2]:
            return (minIndex + maxIndex) // 2
        elif element < some_list[(minIndex + maxIndex)//2]:
            # print(f'before maxIndex is : {maxIndex}')
            maxIndex = (minIndex + maxIndex // 2)
            # print(f'maxIndex is : {maxIndex}')
        elif element > some_list[(minIndex + maxIndex)//2]:
            # print('hi')
            minIndex = (minIndex + maxIndex // 2)
    return None

def binary_search2(element, some_list):
    start_index = 0
    end_index = len(some_list) - 1

    while start_index <= end_index:
        midpoint = (start_index + end_index) // 2
        if some_list[midpoint] == element:
            return midpoint
        elif some_list[midpoint] > element:
            end_index = midpoint - 1
        else:
            start_index = midpoint + 1
    return None


print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))

print(binary_search2(2, [2, 3, 5, 7, 11]))
print(binary_search2(0, [2, 3, 5, 7, 11]))
print(binary_search2(5, [2, 3, 5, 7, 11]))
print(binary_search2(3, [2, 3, 5, 7, 11]))
print(binary_search2(11, [2, 3, 5, 7, 11]))