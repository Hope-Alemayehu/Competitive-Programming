
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        r=n%3
        if n==1:
            return True
        elif n<3:
            return False
        
        if r==0:
            return self.isPowerOfThree(n/3)
        return False
