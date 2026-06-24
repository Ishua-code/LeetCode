"""567. Permutation in String

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k=len(s1)
        n=len(s2)
        l1=[0]*26
        l2=[0]*26
        if len(s1)>len(s2):
            return False
        for i in range(k):
            l1[ord(s1[i])-ord("a")]+=1
            l2[ord(s2[i])-ord("a")]+=1
        if l1==l2:
            return True
        for i in range(k,n):
            l2[ord(s2[i-k])-ord("a")]-=1
            l2[ord(s2[i])-ord("a")]+=1
            if l1==l2:
                return True
        return l1==l2

            