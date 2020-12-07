def merge(list_a, list_b):

    result = []
    while len(list_a) > 0 and len(list_b) > 0:
        if list_a[0] < list_b[0]:
            result.append(list_a.pop(0))
        else:
            result.append(list_b.pop(0))
    if len(list_a) > 0:
        result.extend(list_a)
    elif len(list_b) > 0:
        result.extend(list_b)

    return result


def merge_sort(my_list):

    if len(my_list) < 2:
        return my_list

    mid_point = len(my_list) // 2
    left_list = merge_sort(my_list[:mid_point])
    right_list = merge_sort(my_list[mid_point:])
    return merge(left_list, right_list)

# print(merge_sort([3, 2, 6, 4, 7, 3]))
