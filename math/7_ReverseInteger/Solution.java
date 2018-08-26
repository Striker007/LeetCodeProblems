class Solution {
    public int reverse(int x) {
        long xReversed = 0;
		while(x != 0) {
			xReversed = xReversed * 10 + x % 10; 
            if (xReversed < Integer.MIN_VALUE || xReversed > Integer.MAX_VALUE) {
                return 0;
            }
            x /= 10;
		}
		return (int) xReversed;	
    }
}
