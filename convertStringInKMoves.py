#https://leetcode.com/contest/biweekly-contest-32/problems/can-convert-string-in-k-moves/

def canConvertString(s: str, t: str, k: int) -> bool:
    letters="abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    if len(s)!=len(t):
        return False
    for num, i in enumerate(t):
        index=letters.find(s[num])
        if i not in letters[index:index+k+1]:
            print(t[index:index+k])
            return False
    return True
s = "input"
t = "ouput"
k = 10
print(canConvertString(s,t,k))
