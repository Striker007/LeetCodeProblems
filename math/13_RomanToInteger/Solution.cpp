class Solution {
public:
    int romanToInt(string s) {
        
        map<char, int> roman = {
            { 'I', 1 }, { 'V', 5 }, { 'X', 10 }, { 'L', 50 },
            { 'C', 100 }, { 'D', 500 }, { 'M', 1000 }
        };
        int i = 0;
        int num = 0;
        char prev;
         
        for(char& l : s) {
            
            if (
                (prev == 'I' and (l == 'V' or l == 'X')) or
                (prev == 'X' and (l == 'L' or l == 'C')) or
                (prev == 'C' and (l == 'D' or l == 'M'))
               ) {
                
                 num = num + (roman[l] - (roman[prev] * 2));
                
            } else {
                
                 num = num + roman[l];
                
            }
                    
            prev = l;
                    
        }
        
        return num;
    }
};