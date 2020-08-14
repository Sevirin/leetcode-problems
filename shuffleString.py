#https://leetcode.com/contest/weekly-contest-199/problems/shuffle-string/
""" Given a string s and an integer array indices of the same length.

The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string.
Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
"""
from typing import List

def restoreString(self, s: str, indices: List[int]) -> str:
    outp=[""]*len(indices)
    b=0
    for i in indices:
        outp[i]=s[b]
        b+=1
    return "".join(outp)
s ="codeleet"
ass = [4,5,6,7,0,2,1,3]
print(restoreString(1,s, ass))

