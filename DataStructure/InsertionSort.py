
import bisect


def insertion_sort(ele):

    sorted_list = []
    for e in ele:
        bisect.insort(sorted_list, e)
        print(sorted_list)

    return sorted_list


ele = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]
s_list = insertion_sort(ele)
print('Sorted list is:', s_list)

