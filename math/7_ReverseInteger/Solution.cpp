class Solution {
public:
    int reverse(int x) {
        long long xReversed = 0;
        while(x) {
            xReversed = xReversed * 10 + x % 10; x /= 10;
            cout << xReversed;
        }
        return (xReversed < INT_MIN || xReversed > INT_MAX) ? 0 : xReversed;
    }
};