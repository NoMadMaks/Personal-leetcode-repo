def reverse(x: int) -> int:
        neg = 1
        if x < 0:
            neg = -1
            strx = str(x)[1:]
        else:
            strx = str(x)

        x = int(strx[::-1])
        
        return 0 if x > pow(2, 31) else x * neg

x = -123
y = reverse(x)
print(y)