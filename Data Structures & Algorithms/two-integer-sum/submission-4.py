class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = [(num,i) for i,num in enumerate(nums)] # list comprehension to put the value in front and index as second element
        sorted_nums.sort() #sort by the value 

        head = 0
        tail = len(sorted_nums) - 1

        while head <= tail:
            if sorted_nums[head][0] + sorted_nums[tail][0] == target:
                return sorted(list((sorted_nums[head][1],sorted_nums[tail][1])))

            if sorted_nums[head][0] + sorted_nums[tail][0] > target:
                tail -= 1
            
            if sorted_nums[head][0] + sorted_nums[tail][0] < target:
                head += 1


        
            

        