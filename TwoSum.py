def twoSum(nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == target - nums[j]:
                    return [i,j]

nums = [2,7,11,15]
target = 13

x = twoSum(nums, target)
print(x)