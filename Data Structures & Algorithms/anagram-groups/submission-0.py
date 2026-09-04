class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        original_and_sorted = {}
        output = []
        done = []

        for string in strs:
            # sort the string by ascending alphabetical order
            str_list = list(string)
            str_list.sort()
            sorted_str = "".join(str_list)

            # make a dictionary where key is the sorted string for comparison and value is orginal str
            if sorted_str not in original_and_sorted:
                original_and_sorted[sorted_str] = []
            original_and_sorted[sorted_str].append(string)
        
        return list(original_and_sorted.values())