def algorithm(N):
    count = 0
    for i in range(N):
        for j in range(N):
            count += 1
    return count


def bubble_sort(nums):
    N = len(nums)
    for i in range(N - 1):
        for j in range(N - 1 - i):
            if nums[j] > nums[j + 1];
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums 