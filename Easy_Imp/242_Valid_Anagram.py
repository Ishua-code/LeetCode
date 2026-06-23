"""242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        cs , ct={},{}
        for i in range(len(s)):
            cs[s[i]]= 1+cs.get(s[i],0)
            ct[t[i]]= 1+ct.get(t[i],0)
        for i in cs:
            if cs[i] != ct.get(i,0):
                return False
        return True
 