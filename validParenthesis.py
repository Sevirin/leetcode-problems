#https://leetcode.com/problems/valid-parentheses/

def isValid(s: str) -> bool:
    stack=[]
    a={")":"(","]":"[","}":"{"}
    if len(s)%2!=0 or len(s)<2:
        return False
    for i in s:
        if i=="[" or i=="{" or i=="(":
            stack.append(i)  
        elif len(stack)>0:
            if stack[-1]==a[i]:
                stack.pop()
            else:
                return False
        else:
            return False
    if len(stack)!=0:
        return False
    else:
        return True
print(isValid("))"))

def isValid2(s: str) -> bool:
    top=-1
    stack=[]
    if len(s)%2!=0:
        return False
    for i in s:
        if i=='(' or i=='{' or i=='[':
            stack.append(i)
            top+=1
        elif len(stack)>0:
            com=stack.pop()
            if i==')' and com=='(':
                top-=1
            elif i=='}' and com=='{':
                top-=1
            elif i==']' and com=='[':
                top-=1
            else:
                return False
        else :
            return False
    return top==-1
    

