
nums = [3,3]
target = 6
""" if len(nums)==2:
    print("sdsd") """
""" for i in range(len(nums)):
    for j in nums[i+1:]:
        if nums[i]+j==target:
            print([i,]) """
def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        
        for index, num in enumerate(nums):
            other = target - num
            
            if other in seen:
                return [seen[other], index]
            else:
                seen[num] = index
                
        return []
print(twoSum(nums,target))