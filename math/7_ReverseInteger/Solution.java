class Solution {
    public int reverse(int x) {
        long xReversed = 0;
		while(x != 0) {
			xReversed = xReversed * 10 + x % 10; x /= 10;
            System.out.println(xReversed);
		}
		return (xReversed < Integer.MIN_VALUE || xReversed > Integer.MAX_VALUE) ? 0 : (int) xReversed;	
    }
}
