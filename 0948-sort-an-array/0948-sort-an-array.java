class Solution {
    public int[] sortArray(int[] nums) {
        //bucket sort
        
        //Initialize buckets
        List<Integer>[] buckets = new ArrayList[100001];
        for(int i = 0; i < buckets.length; i++) {
            buckets[i] = new ArrayList<>();
        }

        //Fill the buckets
        for (int num : nums) {
            int i = num + 50000;
            buckets[i].add(num);
        }

        //Empty the buckets back into nums
        int index = 0;
        for (int i = 0; i < buckets.length; i++) {
            for (int num : buckets[i]) {
                nums[index] = num;
                index++;
            }
        }   

        //return the sorted array
        return nums;

    }
}