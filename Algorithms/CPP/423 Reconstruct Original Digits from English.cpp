class Solution {
public:
    string originalDigits(string s) {
        string result;
        array<pair<char, int>, 10> abbreviation_dict = {
            make_pair('z', 0), make_pair('w', 2), make_pair('u', 4), make_pair('x', 6), make_pair('g', 8), make_pair('o', 1), make_pair('f', 5), make_pair('s', 7), make_pair('t', 3), make_pair('i', 9)};
        string full_dict[10] = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
        array<int, 26> digit_dict = count(s);
        int counter[10] = {0};

        for (int i = 0; i < 10; ++i){
            char c = abbreviation_dict[i].first;
            int n = abbreviation_dict[i].second;
            counter[n] = digit_dict[c - 'a'];
            if (counter[n]){
                for (int i = 0; i < full_dict[n].size(); ++i){
                    digit_dict[full_dict[n].at(i) - 'a'] -= counter[n];
                }
            }
        }

        for (int i = 0; i < 10; ++i){
            result += string(counter[i], i + '0');
        }

        return result;
    }

private:
    array<int, 26> count(string s){
        array<int, 26> result = {0};
        for (int i = 0; i < s.size(); ++i){
            ++result[s[i] - 'a'];
        }

        return result;
    }
};
