
import array


def max_product(arr):
    x = arr[0]
    y = arr[1]

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] * arr[j] > x * y:
                x = arr[i]
                y = arr[j]
    return x, y


arr = array.array('i', [2, 3, -16, 4, 8, 7, -9])
print('Max Product Pair is : ', max_product(arr))