class Solution {
public:
    string intToRoman(int num) {
        char base1[] = {'I', 'X', 'C', 'M'};
        string base4[] = {"IV", "XL", "CD"};
        string base5[] = {"V", "L", "D"};
        string base9[] = {"IX", "XC", "CM"};

        int flag = 0;
        string result = "";
        string roman = "";
        while (num){
            int n = num % 10;
            if (n == 0){
                roman = "";
            }
            else if(n <= 3){
                roman = string(n, base1[flag]);
            }
            else if(n == 4){
                roman = base4[flag];
            }
            else if(n == 5){
                roman = base5[flag];
            }
            else if(n <= 8){
                roman = base5[flag] + string(n - 5, base1[flag]);
            }
            else{
                // n == 9
                roman = base9[flag];
            }
            result = roman + result;
            num = num / 10;
            flag = flag + 1;
        }
        return result;        
    }
};
