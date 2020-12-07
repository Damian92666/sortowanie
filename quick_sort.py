def quick_sort(my_list):
    if len(my_list) < 2:
        return my_list
    last_element = my_list.pop()
    left_list = []
    right_list = []
    for element in my_list:
        if element < last_element:
            left_list.append(element)
        else:
            right_list.append(element)
    return quick_sort(left_list) + [last_element] + quick_sort(right_list)


# print(quick_sort([2, 3, 6, 7, 4, 3]))
