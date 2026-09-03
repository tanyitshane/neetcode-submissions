class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_s = s.lower()
        list_letter = []
        for letter in lower_s:
            if letter.isalnum():
                list_letter.append(letter)
        
        reversed_list = list_letter[::-1]

        if list_letter == reversed_list:
            return True
        
        else:
            return False