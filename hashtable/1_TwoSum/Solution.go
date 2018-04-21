func twoSum(nums []int, target int) []int {
    error := []int{-1,-1}
    m := map[int]int{}
    for i := 0; i < len(nums); i++ {
        complement := target - nums[i]
        if val, ok := m[complement]; ok {
            return []int{val,i}
        }
        m[nums[i]] = i
    }
    return error
}