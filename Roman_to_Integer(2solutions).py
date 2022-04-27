def romanToInt(s: str):
        li = []
        for letter in s:
            li.append(letter)  
        total = 0
        for n in range (len(li)-1):
            if li[n] == 'I':
                if li[n+1] == 'V':
                    total = total - 1
                    continue
                elif li[n+1] == 'X':
                    total = total - 1
                    continue
                else:
                    total = total + 1
                    continue
            elif li[n] == 'V':
                total = total + 5
                continue
            elif li[n] == 'X':
                if li[n+1] == 'L':
                    total = total - 10
                    continue
                elif li[n+1] == 'C':
                    total = total - 10
                    continue
                else: 
                    total = total + 10
                    continue
            elif li[n] == 'L':
                total = total + 50
                continue
            elif li[n] == 'C':
                if li[n+1] == 'D':
                    total = total - 100
                    continue
                elif li[n+1] == 'M':
                    total = total - 100
                    continue
                else:
                    total = total + 100
                    continue
            elif li[n] == 'D':
                total = total + 500
                continue
            elif li[n] == 'M':
                total = total + 1000
                continue
        for n in range(len(li)-1, len(li)):
            if li[n] == 'I':
                total = total + 1
            elif li[n] == 'V':
                total = total + 5
            elif li[n] == 'X':
                total = total + 10
            elif li[n] == 'L':
                total = total + 50
            elif li[n] == 'C':
                total = total + 100
            elif li[n] == 'D':
                total = total + 500
            elif li[n] == 'M':
                total = total + 1000
                    
        return total

def romanToIntwithdict(s: str):
    roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
    z = 0
    for i in range(0, len(s) - 1):
        if roman[s[i]] < roman[s[i+1]]:
            z -= roman[s[i]]
        else:
            z += roman[s[i]]
    return z + roman[s[-1]]

s = "MCMXCIV"
x = romanToInt(s)
print(x)

y = romanToIntwithdict(s)
print(y)

