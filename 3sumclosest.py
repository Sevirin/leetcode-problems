#https://leetcode.com/problems/3sum-closest/
from typing import List

def threeSumClosest(arr: List[int], target: int) -> int:
    closestSum=arr[1]+arr[2]+arr[0]
    if len(arr)==3:
        return closestSum
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)-1):
            for k in range(j + 1, len(arr)):
                # Update the closestSum
                if(abs(target - closestSum) >= 
                   abs(target - (arr[i] +
                   arr[j] + arr[k]))):
                       closestSum = (arr[i] +
                                     arr[j] + arr[k])
    return closestSum
nums = [1,1,-1,-1,3]
target = -1
print(threeSumClosest(nums,target))
