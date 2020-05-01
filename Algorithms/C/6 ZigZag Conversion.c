char * convert(char * s, int numRows){
    if (numRows <= 1 || numRows > strlen(s)){
        return s;
    }

    int n = strlen(s);
    char* result = (char*)malloc(n + 1);
    memset(result, 0, n + 1);
    int pos = 0;

    for (int r = 0; r < numRows; ++r){
        int start = r;
        if (r == 0 || r == (numRows - 1)){
            int step = (numRows - 2) * 2 + 2;
            while (start < n) {
                result[pos++] = s[start];
                start += step;
            }
        }
        else {
            int margin_1 = (numRows - r - 2) * 2 + 2;
            int margin_2 = r * 2;
            bool flage = true;
            while (start < n) {
                result[pos++] = s[start];
                if (flage) {
                    start = start + margin_1;
                }
                else {
                    start = start + margin_2;
                }
                flage = !flage;
            }
        }
    }

    return result;
}
