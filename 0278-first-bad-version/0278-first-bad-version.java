/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        int l = 1;
        int r = n; 
        int badVersion = 0;

        while (l <= r) {
            int m = l + (r - l) / 2;
            if (isBadVersion(m)) {
                badVersion = m;
                r = m - 1;
            } else {
                l = m + 1;
            }
        }
        return badVersion;
    }
}