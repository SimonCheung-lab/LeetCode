# 1 
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n < 0:
            return 1.0 / self.myPow(x, -n)
        
        if n % 2 == 0:
            return self.myPow(x * x, n / 2)
        
        return x * self.myPow(x, n - 1)
        

# 2
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        
        pow = 1
        while n:
            if n & 1:
                pow *= x
            
            x *= x
            n >>= 1
        
        return pow    
        
