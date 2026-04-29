class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> nums2 = new HashMap<>(); // num, index 

        for (int i = 0; i < nums.length; i++) {
            if (nums2.containsKey(target - nums[i])) {
                int[] res = {nums2.get(target - nums[i]), i};
                return res;
            }
            else {
                nums2.put(nums[i], i);
            }
            


        }

    return new int[0];
    }
}
