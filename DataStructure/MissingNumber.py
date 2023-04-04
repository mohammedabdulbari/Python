
import array


def missing_num(given_list):

    start = given_list[0]
    end = given_list[ len(given_list) - 1 ]

    actual_list = list(range(start, end + 1))
    actual_sum = sum(actual_list)
    given_sum = sum(given_list)

    return actual_sum - given_sum


arr = array.array('i', [11, 12, 13, 14, 16, 17])

miss_num = missing_num(arr)

if miss_num > 0:
    print('Missing number is', missing_num(arr))
else:
    print('No Missing Number Found')

