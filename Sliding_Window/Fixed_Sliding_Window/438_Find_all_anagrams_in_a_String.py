"""438. Find All Anagrams in a String

Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab"."""

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l=[]
        k=len(p)
        n=len(s)
        l1=[0]*26
        l2=[0]*26
        if len(p)>len(s):
            return []
        for i in range(k):
            l1[ord(p[i])-ord("a")]+=1
            l2[ord(s[i])-ord("a")]+=1
        if l1==l2:
            l.append(0)
        for i in range(k,n):
            l2[ord(s[i-k])-ord("a")]-=1
            l2[ord(s[i])-ord("a")]+=1
            if l1==l2:
                l.append(i-k+1)
        return l