class Solution(object):
    def twoSum(self, numbers, target):
        left=0
        right=len(numbers)-1
        while left<right:
            a=numbers[left]+numbers[right]
            if a<target:
                left+=1
            elif a>target:
                right-=1
            else:
                return [left+1,right+1]
