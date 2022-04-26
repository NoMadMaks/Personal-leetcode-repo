def removeDuplicates(nums):
        li = []
        counter = 0
        total = len(nums)
        for n in range(0,total):
            try:
                while nums[n+1] == nums[n]:
                    nums.pop(n+1)
                    total = total - 1
            except IndexError:
                total = total - 1
                continue
        for n in range(len(nums)):
            counter = counter + 1
        return counter

nums = [0,0,1,1,1,2,2,3,3,4]
x = removeDuplicates(nums)
print(x)
print(nums)