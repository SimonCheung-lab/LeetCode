import collections

class Solution:
    def originalDigits(self, s: str) -> str:
        abbreviation_dict = {'z': 0, 'w': 2, 'u': 4, 'x': 6, 'g': 8, 'o': 1, 'f': 5, 's': 7, 't': 3, 'i': 9}
        full_dict = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
        digit_dict = collections.Counter(s)
        counter = {key: 0 for key in range(10)}
        
        for key, value in abbreviation_dict.items():
            counter[value] = digit_dict[key]
            if counter[value]:
                for c in full_dict[value]:
                    digit_dict[c] = digit_dict[c] - counter[value]

        result = ''
        for key, value in counter.items():
            result = result + str(key) * value

        return result

        
