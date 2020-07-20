class Solution {
    public int divide(int dividend, int divisor) {
        if (divisor == -1) {
            if (dividend == Integer.MIN_VALUE) {
                return Integer.MAX_VALUE;
            }
            else {
                return -dividend;
            }
        }

        long dividend_long = dividend;
        long divisor_long = divisor;
        int flag = 1;

        if (dividend_long < 0) {
            flag = -flag;
            dividend_long = -dividend_long;
        }

        if (divisor_long < 0) {
            flag = -flag;
            divisor_long = -divisor_long;
        }

        return flag * div(dividend_long, divisor_long);
    }

    private int div(long dividend, long divisor) {
        if (dividend < divisor) {
            return 0;
        }

        long divisor_tmp = divisor;
        int ans = 1;
        
        while (divisor_tmp * 2 < dividend) {
            ans = 2 * ans;
            divisor_tmp = 2 * divisor_tmp;
        }

        return ans + div(dividend - divisor_tmp, divisor);
    }
};
