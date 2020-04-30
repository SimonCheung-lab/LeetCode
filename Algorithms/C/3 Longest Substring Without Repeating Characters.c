// O(n)
int max(int a, int b)
{
    if (a > b){
        return a;
    }
    return b;
}

int lengthOfLongestSubstring(char * s){
    if (s == NULL) {
	return 0;
	}
	
	// 256 / 8 = 32
	unsigned char has[32];
	memset(has, 0, 32);
	
	int n = strlen(s);
	int i, j, max_len;
	i = j = max_len = 0;
	while (j < n) {
		while ((j < n) && (((has[s[j] / 8] >> (7 - (s[j] % 8))) & 1) == 0)) { // not exists
			has[s[j] / 8] |= ((unsigned char)1 << (7 - (s[j] % 8))); // set 1
			++j;
		}

        max_len = max(max_len, j - i);

		if (j >= n) {
			break;
		}

		while (s[i] != s[j]) {
			has[s[i] / 8] ^= ((unsigned char)1 << (7 - (s[i] % 8))); // set 0
			++i;
		}

        has[s[i] / 8] ^= ((unsigned char)1 << (7 - (s[i] % 8))); // set 0

        ++i;
	}

	return max_len;
}
