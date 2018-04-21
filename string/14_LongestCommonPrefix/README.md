Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note:
All given inputs are in lowercase letters a-z.

---
## horizontal
Time complexity : O(S), where S is the sum of all characters in all strings.
In the worst case all nn strings are the same. The algorithm compares the string S1 with the other strings S2..Sn
​​There are SS character comparisons, where SS is the sum of all characters in the input array.
Space complexity : O(1). We only used constant extra space.

## vertical
Time complexity : O(S), where S is the sum of all characters in all strings.
In the worst case there will be nn equal strings with length mm and the algorithm performs S = m*n character comparisons.
Even though the worst case is still the same as Approach 1, in the best case there are at most n*minLenn∗minLen comparisons
where minLenminLen is the length of the shortest string in the array.
Space complexity : O(1)O(1). We only used constant extra space.

