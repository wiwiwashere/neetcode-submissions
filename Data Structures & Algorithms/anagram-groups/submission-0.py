from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for s in strs:
            group["".join(sorted(s))].append(s)
        res = []
        for key, value in group.items():
            res.append(value)
        return res