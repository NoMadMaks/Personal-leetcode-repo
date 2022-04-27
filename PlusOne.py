def plusOne(digits):
        li = []
        stringnmbr = ''
        for n in range(len(digits)):
            stringnmbr = stringnmbr + str(digits[n])
        ans = int(stringnmbr) + 1
        ans2 = str(ans)
        for n in range(len(ans2)):
            li.append(ans2[int(n)])
        return li




  
digits = [4,3,2,1]
x = plusOne(digits)
print(x)
        


