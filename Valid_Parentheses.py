def isValid(s: str) -> bool:
        otvor = ['(', '[', '{']
        zatvor = [')', ']', '}']
        parovi = [('(', ')'), ('[', ']'), ('{', '}')]
        stack = []
        for param in s:
            if param in otvor:
                stack.append(param)
            elif param in zatvor:
                try:
                    zadnji = stack.pop()
                except: return False
                if (zadnji, param) not in parovi:
                    return False
        if len(stack) == 0:
            return True

s = "(({})"
if isValid(s):
    print('true')
else:
    print('false')