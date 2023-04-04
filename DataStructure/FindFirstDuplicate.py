import array


def find_duplicate(nums):
    num_set = set()

    for n in nums:
        if n in num_set:
            return n
        else:
            num_set.add(n)
    else:
        return -1


arr = array.array('i', [2, 3, 4, 5, 6, 7, 15, 8, 9, 10, 12])
print(find_duplicate(arr))

