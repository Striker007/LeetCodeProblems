class Solution {
    public boolean isPalindrome(int x) {
        
        if (x < 0) {
            return false;
        }
        int dec = 1;
        while (x / dec >= 10) {
            dec *= 10;
        }
        while (x != 0) {
            int l = x / dec;
            int r = x % 10;
            if (l != r)
                return false;
            x = (x % dec) / 10;
            dec /= 100;
        }
        return true;
    }
}