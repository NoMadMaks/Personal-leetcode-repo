def searchInsert(nums, target):
        if target in nums:
             for n in range(len(nums)):
                if nums[n] == target:
                    return n    

        else:
            for n in range(len(nums)):
                if nums[n] == target:
                    return n
                elif target < nums[n]:
                    return n 
                else: 
                    continue
            n = len(nums)
            return n

nums = [1,3,5,6]
target = 7

x = searchInsert(nums, target)
print(x)