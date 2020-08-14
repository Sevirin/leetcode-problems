""" 
https://leetcode.com/problems/median-of-two-sorted-arrays/
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty. 
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
"""


def findMedianSortedArrays(nums1,nums2) -> float:
    i=0
    j=0
    temp=[None]*(len(nums1)+len(nums2))
    x=0
    while i<len(nums1) and j<len(nums2):
        if nums1[i]<nums2[j]:
            temp[x]=nums1[i]
            i+=1
            x+=1
        else:
            temp[x]=nums2[j]
            j+=1
            x+=1
    while i<len(nums1):
        temp[x]=nums1[i]
        i+=1
        j+=1
    while j<len(nums2):
        temp[x]=nums2[j]
        j+=1
        x+=1
    if len(temp)%2==0:
        a=temp[(len(temp)//2)-1]
        b=temp[(len(temp)//2)]
        return(a+b)/2
    else:
        return float(temp[int((len(temp)/2))])

nums1 = [1, 2]
nums2 = [3, 4,7,9]
print(findMedianSortedArrays(nums1,nums2))