func twoSum(nums []int, target int) []int {

    buffer := map[int]int{}

    for i := 0; i < len(nums); i++ {
        complement := target - nums[i]
        if val, ok := buffer[complement]; ok {
            return []int{val,i}
        }
        buffer[nums[i]] = i
    }
    return nil
}