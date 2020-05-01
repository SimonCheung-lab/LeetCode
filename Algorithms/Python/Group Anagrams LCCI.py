class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for w in strs:
            sorted_w = ''.join(sorted(w)) # faster than str(sorted(w))
            result[sorted_w] = result.get(sorted_w, []) + [w]
        return [value for value in result.values()]
