
def isPalindrome(x: int) -> bool:
    return str(x) == str(x)[::-1]  #x(start:stop:step) step -1 krece od zadnjeg prema prvom

             
x = 10
if isPalindrome(x):
    print('yes')
else: print ('no')

