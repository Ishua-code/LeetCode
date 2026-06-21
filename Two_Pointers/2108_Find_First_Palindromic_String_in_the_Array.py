"""2108. Find First Palindromic String in the Array

Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".
A string is palindromic if it reads the same forward and backward.

Example 1:

Input: words = ["abc","car","ada","racecar","cool"]
Output: "ada"
Explanation: The first string that is palindromic is "ada".
Note that "racecar" is also palindromic, but it is not the first.
Example 2:

Input: words = ["notapalindrome","racecar"]
Output: "racecar"
Explanation: The first and only string that is palindromic is "racecar".
Example 3:

Input: words = ["def","ghi"]
Output: ""
Explanation: There are no palindromic strings, so the empty string is returned"""

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        gf=1
        for i in words:
            l=0
            r=len(i)-1
            f=1
            while l<r:
                if i[l]!=i[r]:
                    f=0
                    break
                else:
                    l+=1
                    r-=1
            if f==1:
                gf=0
                return i
        if gf==1:
            return ""
        