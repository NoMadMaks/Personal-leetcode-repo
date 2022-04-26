def removeElement(nums, val):
        counter = 0
        rang = len(nums)
        while val in nums:
            try:
                for n in range(0, rang):
                    if nums[n] == val:
                        nums.pop(n)
                        n = n - 1
                for n in range(len(nums)):
                    counter = counter + 1
                return counter
            except IndexError:
                rang = rang - 1
                continue

nums = [2,2,3]
val = 3

x = removeElement(nums, val)
print(x)
print(nums)    
            