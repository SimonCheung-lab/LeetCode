# define INT_MAX 2147483647
#define INT_MIN (-INT_MAX - 1)
int reverse(int x){
    int result = 0;
    while (x){
        if (result > INT_MAX / 10 || result < INT_MIN / 10){
            return 0;
        }
        result = result * 10 + (x % 10);
        x /= 10;
    }
    return result;
}
