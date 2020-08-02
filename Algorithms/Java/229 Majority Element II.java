class Solution {
    public List<Integer> majorityElement(int[] nums) {
        if (nums.length < 2) {
            var list = new ArrayList<Integer>();
            for (var n : nums) {
                list.add(n);
            }
            return list;
        }

        int candidate1, candidate2;
        candidate1 = candidate2 = nums[0];

        int count1, count2;
        count1 = count2 = 0;

        for (var num : nums) {
            if (num == candidate1) {
                count1++;
                continue;
            }

            if (num == candidate2) {
                count2++;
                continue;
            }

            if (count1 == 0) {
                candidate1 = num;
                count1 = 1;
                continue;
            }

            if (count2 == 0) {
                candidate2 = num;
                count2 = 1;
                continue;
            }

            count1--;
            count2--;
        }

        count1 = count2 = 0;
        for (var num : nums) {
            if (num == candidate1) {
                count1++;
            }
            else if (num == candidate2) {
                count2++;
            }
        }

        ArrayList<Integer> list = new ArrayList<Integer>();
        if (count1 > nums.length / 3) {
            list.add(candidate1);
        }

        if (count2 > nums.length / 3) {
            list.add(candidate2);
        }

        return list;
    }
}
