# keep track of 2 variables, largest and secondLargest
# if we find a number greater than largest, we update both
# move largest into secondLargest, and update largest
# if a number is smaller than largest but greater than secondLargest
# we update secondLargest
# time O(n). space O(1)
def second_largest(nums):
    if len(nums) < 2:
        return None
    largest = nums[0]
    secondLargest = largest
    for i in nums:
        if i > largest:
            secondLargest = largest
            largest = i
        if largest > i > secondLargest:
            secondLargest = i
    return secondLargest


print(second_largest([10, 20, 4, 45, 99]))
print(second_largest([3, 3, 3]))
print(second_largest([8]))
