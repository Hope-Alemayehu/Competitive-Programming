class Solution:
    def sortSentence(self, s: str) -> str:
        arr = s.split()   //split the array of strings

        arr.sort(key=lambda x :int(x[-1]))
        return " ".join(x[:-1] for x in arr)
