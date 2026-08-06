class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word1=Counter(s)
        word2=Counter(t)
        if word1==word2:
            return True
        else:
            return False