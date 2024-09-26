def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1  

my_list = [12, 45, 6, 32, 78, 11, 9, 31]
search_target = 32
result = linear_search(my_list, search_target)

if result != -1:
    print(f"{search_target} found at index {result}")
else:
    print(f"{search_target} not found in the list.")
