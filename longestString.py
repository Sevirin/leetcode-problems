""" 
https://leetcode.com/problems/longest-substring-without-repeating-characters/
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3.  """

def lengthOfLongestSubstring(self, s: str) -> int:
    if len(s)<1:
        return 0
    count=0
    highcount=0
    used=""
    for i in range(len(s)):
        if s[i] not in used:
            used+=s[i]
            count+=1
        else:
            used = used[used.index(s[i])+1::]+s[i]
            count=len(used)
        if count>highcount:
            highcount=count
    return highcount

input= "abcabcbb"
print(lengthOfLongestSubstring(input,input))
#print(len(input))
