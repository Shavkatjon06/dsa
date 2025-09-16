# For each element, check the sum with all
# subsequent elements. If their sum equals our
# target, we return indices.
# Nested loops leading to O(n^2)
def two_sum_1(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


print(two_sum_1([2, 7, 11, 15], 9))
print(two_sum_1([3, 2, 4], 6))
print(two_sum_1([3, 3], 6))


print("---")


# Let's create a bag {} to store item:index
# for each element, compute the difference: diff=target-value
# if diff is in our bag, we return the pair of indices
# else store the current item:index in our bag
# time & space complexity O(n)
def two_sum_2(nums, target):
    bag = {}
    for index, value in enumerate(nums):
        diff = target - value
        if diff in bag:
            return [bag[diff], index]
        else:
            bag[value] = index
    return []


print(two_sum_1([2, 7, 11, 15], 9))
print(two_sum_1([3, 2, 4], 6))
print(two_sum_1([3, 3], 6))