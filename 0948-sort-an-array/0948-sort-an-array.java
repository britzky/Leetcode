class Solution {
    public int[] sortArray(int[] nums) {
        return sortHelper(nums, 0, nums.length - 1);
    }

    public int[] sortHelper(int[] nums, int s, int e) {
        if (e - s + 1 <= 1) {
            return nums;
        }
        int m = (s + e) / 2;
        sortHelper(nums, s, m);
        sortHelper(nums, m + 1, e);
        merge(nums, s, m, e);
        return nums;
    }

    public void merge(int[] nums, int s, int m, int e) {
        int[] L = Arrays.copyOfRange(nums, s, m + 1);
        int[] R = Arrays.copyOfRange(nums, m + 1, e + 1);

        int i = 0;
        int j = 0;
        int k = s;

        while (i < L.length && j < R.length) {
            if (L[i] <= R[j]) {
                nums[k] = L[i];
                i++;
            } else {
                nums[k] = R[j];
                j++;
            }
            k++;
        }

        while (i < L.length) {
            nums[k] = L[i];
            i++;
            k++;
        }

        while (j < R.length) {
            nums[k] = R[j];
            j++;
            k++;
        }
    }
}