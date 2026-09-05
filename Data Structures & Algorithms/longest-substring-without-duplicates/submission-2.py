class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left_idx = 0
        right_idx = 0
        max_length = 0 # max length without duplicate characters
        current_letters = set()

        while right_idx < len(s):
            while s[right_idx] in current_letters:
                current_letters.remove(s[left_idx])
                left_idx += 1

            current_letters.add(s[right_idx])
            
            if right_idx - left_idx + 1 > max_length:
                max_length = right_idx - left_idx + 1
            
            right_idx += 1

        return max_length
        
        