def find_duplicate(nums):
    sorted_nums = sorted(nums)
    if len(sorted_nums) < 2:
        return False
    for index in range(len(sorted_nums) - 1):
        if type(sorted_nums[index]) is str or sorted_nums[0] < 1:
            return False
        if sorted_nums[index] == sorted_nums[index + 1]:
            return sorted_nums[index]
    return False


print(find_duplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # False
print(find_duplicate([1, 2, 2, 4, 5, 6, 7, 8, 9, 10]))  # 2
