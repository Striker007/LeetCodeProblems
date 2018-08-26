class Solution {
    public:
        int climbStairs(int n) {
            
            if (n <= 3) {
                return n;
            }
            
            int prev2 = 0;
            int prev1 = 1;
            int z = 0;
                      
            for (int i = 1; i <= n + 1; i++) {

                if (i == n) {
                    return prev2 + prev1;
                }
                
                z = prev2;
                prev2 = prev1;
                prev1 = prev2 + z;
            }
            
            return 0;
        }
};
