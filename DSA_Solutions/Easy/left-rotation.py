# naive approach
def left_rotation_1(nums, k):
    n = len(nums)
    for i in range(k):
        first = nums[0]
        for j in range(n-1):
            nums[j] = nums[j+1]
        nums[n-1] = first
    return nums


print(left_rotation_1([1, 2, 3, 4, 5], 2))
print(left_rotation_1([7, 8, 9], 1))


# better approach
# shift elements starting from index k to the front
# and place the first k elements at the back of temp
def left_rotation_2(nums, k):
    n = len(nums)
    k = k % n

    temp = [0] * n
    for i in range(n-k):
        temp[i] = nums[k+i]

    for i in range(k):
        temp[n-k+i] = nums[i]

    return temp


print(left_rotation_2([1, 2, 3, 4, 5], 2))
print(left_rotation_2([7, 8, 9], 1))