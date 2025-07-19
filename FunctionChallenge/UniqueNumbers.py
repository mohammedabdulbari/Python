
def unique_nums(*args):
    nums = set(args)
    return list(nums)


print("Enter Nums separated by spaces:")
nums = input("")


numbers = [int(n) for n in nums.split()]
unique = unique_nums(*numbers)

print("\nUnique Numbers:")
print(unique)

