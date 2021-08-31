import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        output = collections.defaultdict(list)
        for i in strs:
            output[tuple(sorted(i))].append(i)

        return output.values()
        
