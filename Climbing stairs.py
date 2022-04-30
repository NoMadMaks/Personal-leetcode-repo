def climbStairs(n: int) -> int:
        memo ={}
        memo[1] = 1
        memo[2] = 2
        
        def climb(n):
            if n in memo: 
                return memo[n]
            else:   
                memo[n] =  climb(n-1) + climb(n-2)
                return memo[n]
        
        return climb(n)

n = 30
x = climbStairs(n)
print(x)