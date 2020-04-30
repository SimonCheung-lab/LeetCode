class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_substring = {}
        len_max_substring = 0
        for i, c in enumerate(s):
            if max_substring.get(c) is None:
                max_substring[c] = i
                len_max_substring = max(len_max_substring, len(max_substring))
            else:
                # encounter repeating character
                index = max_substring[c]
                max_substring.clear()
                for j in range(index, i + 1):
                    max_substring[s[j]] = j
        return len_max_substring
