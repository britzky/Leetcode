class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int l = 1;
        int r = 1;
        
        for (int pile : piles) {
            r = Math.max(pile, r);
        }

        while (l < r) {
            int m = l + (r - l) / 2;
            int hoursSpent = 0;

            for (int pile : piles) {
                hoursSpent += Math.ceil((double) pile / m);
            }

            if (hoursSpent <= h) {
                r = m;
            } else {
                l = m + 1;
            }
        }

        return r;

    }
}