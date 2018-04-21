class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int,int> myMap;
        for(int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            if ( myMap.find(complement) != myMap.end()) {
                return {myMap[complement], i};
            }
            myMap[nums[i]] = i;
        }
        throw std::runtime_error("There are'nt target in the nums");
    }
};
