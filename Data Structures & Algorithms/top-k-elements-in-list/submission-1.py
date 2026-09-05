class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        number_and_frequency = {}

        for num in nums:
            if num not in number_and_frequency:
                number_and_frequency[num] = 1
            elif num in number_and_frequency:
                number_and_frequency[num] += 1
        
        sorted_number_and_frequency = sorted(number_and_frequency.items(), key=lambda item: item[1])
        last_two_keys = [num for num, freq in sorted_number_and_frequency[-k:]]
        
        return last_two_keys
