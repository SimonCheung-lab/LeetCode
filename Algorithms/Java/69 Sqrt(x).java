class Solution {
    public int mySqrt(int x) {
        if (x == 0) {
            return 0;
        }
        if (x <= 2) {
            return 1;
        }
        
        int left, right;
        left = 1;
        right = x / 2;

        while (left <= right) {
            int mid = (right - left) / 2 + left;
            double square = Math.pow(mid, 2);
            if (x == square) {
                return mid;
            }
            else if (x < square) {
                right = mid - 1;
            }
            else {
                left = mid + 1;
            }
        }

        return Math.pow(left, 2) > x ? left - 1 : left;
    }
}
