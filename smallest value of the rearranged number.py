class Solution:
    def smallestNumber(self, num: int) -> int:
       
        arr= sorted(str(abs(num)))
        if num<=0:
            return -int(''.join(arr[::-1]))
        i=0
        while arr[i]=="0":
            i+=1

        arr[0],arr[i] = arr[i],arr[0]
        return int(''.join(arr))
    
