#https://leetcode.com/contest/biweekly-contest-32/problems/kth-missing-positive-number/
from typing import List
def findKthPositive(arr: List[int], k: int) -> int:
    missingCounter=0
    intiger=1
    while missingCounter<k:
        if intiger not in arr:
            missingCounter+=1
            if missingCounter==k:
                return intiger
        intiger+=1
arr = [1,3,5,7]
k = 2
print(findKthPositive(arr,k))