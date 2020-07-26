class Solution {
    public int findMin(int[] nums) {
        int n = nums.length;
        int left, right, mid;
        left = 0;
        right = n - 1;

        int ans = nums[0];

        while (left <= right) {
            mid = (left + right) / 2;
            
            if (nums[left] <= nums[mid]) {
                ans = Math.min(ans, nums[left]);
                left = mid + 1;
            }
            else {
                ans = Math.min(ans, nums[mid]);
                right = mid - 1;
            }
        }

        return ans;
    }
}
