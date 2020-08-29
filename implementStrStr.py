#https://leetcode.com/problems/implement-strstr/

def strStr(haystack: str, needle: str) -> int:
    if needle not in haystack:
        return -1
    if len(needle)<=0:
        return 0
    counter=1
    for i in range(len(haystack)):
        if haystack[i]==needle[counter-1]:
            if len(needle)==1:
                return i
            for j in range(len(needle)):
                if haystack[i+j+1]==needle[j+1]:
                    counter+=1
                else: 
                    counter=1
                    break
                if counter==len(needle):
                    return i            
haystack = "a"
needle = "a"
print(strStr(haystack,needle))