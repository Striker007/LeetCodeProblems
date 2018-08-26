class Solution {
public:
    int reverse(int x) {
        long long xReversed = 0;
        while(x) {
            int pop = x % 10;
            x /= 10;
            // cout << xReversed;
            if (xReversed > INT_MAX/10 || (xReversed == INT_MAX / 10 && pop > 7)) return 0;
            if (xReversed < INT_MIN/10 || (xReversed == INT_MIN / 10 && pop < -8)) return 0;
            xReversed = xReversed * 10 + pop;
        }
        return xReversed;
    }
};