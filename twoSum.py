""" 
https://leetcode.com/problems/two-sum/

Given an array of integers, return indices of the two numbers such
 that they add up to a specific target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice. """

def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j,k in enumerate(nums[i+1:],i+1):
            if nums[i]+k==target:
                print([i,j])