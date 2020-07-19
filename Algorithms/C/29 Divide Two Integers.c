long div_(long long dividend, long long divisor)
{
    if (dividend < divisor) {
        return 0;
    }

    long long divisor_tmp = divisor;
    int ans = 1;
    while (divisor_tmp * 2 < dividend) {
        ans = 2 * ans;
        divisor_tmp = 2 * divisor_tmp;
    }

    return ans + div_(dividend - divisor_tmp, divisor);
}

int divide(int dividend, int divisor){
    long long limits = pow(2, 31);
    int MAX = limits - 1;
    int MIN = -limits;

    if (divisor == -1) {
        if (dividend <= -limits) {
            return MAX;
        }
        else {
            return -dividend;
        }
    }

    long long dividend_long = dividend;
    long long divisor_long = divisor;

    int flag = 1;
    if (dividend_long < 0) {
        flag = -flag;
        dividend_long = -dividend_long;
    }

    if (divisor_long < 0) {
        flag = -flag;
        divisor_long = -divisor_long;
    }

    return flag * div_(dividend_long, divisor_long);
}
