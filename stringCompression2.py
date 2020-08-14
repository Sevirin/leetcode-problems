""" https://leetcode.com/contest/weekly-contest-199/
problems/string-compression-ii/ 
Run-length encoding is a string compression method that works by replacing consecutive identical characters 
(repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters 
(length of the run). For example, to compress the string "aabccc" we replace "aa" by "a2" and replace "ccc" by "c3". 
Thus the compressed string becomes "a2bc3".
Notice that in this problem, we are not adding '1' after single characters.

Given a string s and an integer k. You need to delete at most k characters from s such that the run-length encoded 
version of s has minimum length.
Find the minimum length of the run-length encoded version of s after deleting at most k characters.

Input: s = "aabbaa", k = 2
Output: 2
Explanation: If we delete both 'b' characters, the resulting compressed string would be "a4" of length 2.
"""
def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
    pass
""" 
Input: s = "aaabcccd", k = 2
Output: 4

s = "aaabcccd"
k = 2
#Output: 4


temp=[]
con=0
letter=s[0]
for i in s:
    if i == letter:
        con+=1
        letter=i
    else:
        if con >0 : temp.append(letter+str(con))
        else: temp.append(letter)
        con=0
        letter=i """


