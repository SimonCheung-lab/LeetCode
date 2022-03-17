// 本质仍是快速幂算法
int myPow(int x, int n)
{
    int result = 1;
    while (n)
    {
        if (n % 2)
        {
            result = result * x % 1337;
        }
        x = (long) x * x % 1337;
        n /= 2;
    }
    return result;
}

int superPow(int a, int* b, int bSize){
    int result = 1;
    for (int i = bSize - 1; i >= 0; --i)
    {
        result = (long) result * myPow(a, b[i]) % 1337;
        a = myPow(a, 10);
    }
    return result;
}
