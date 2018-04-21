class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.size() == 0) return "";
        string word = strs[0];
        for (int i = 0; i < word.length(); i ++) {
            for (int ii = 1; ii < strs.size(); ii++) {
                if (strs[ii][i] != word[i]) {
                    return word.substr(0, i);
                }
            }
        }
        return word;
    }
};
