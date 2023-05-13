class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        r=n%4
        if n==1:
            return True
        elif n<4:
            return False
        
        if r==0:
            return self.isPowerOfFour(n/4)
        return False
