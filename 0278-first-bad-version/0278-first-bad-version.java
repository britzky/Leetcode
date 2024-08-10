/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        int i = 1;
        int j = n;
        int badVersion = 1;

        while(i <= j) {
            int m = i + (j - i) / 2;
            if (isBadVersion(m)){
                badVersion = m;
                j = m - 1;
            } else {
                i = m + 1;
            }
        }
            return badVersion;
    }
}