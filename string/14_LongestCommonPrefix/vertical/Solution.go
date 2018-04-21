func longestCommonPrefix(strs []string) string {
    if len(strs) == 0 {
        return ""
    }
    if len(strs) == 1 {
        return strs[0]
    }
    for position, letter := range strs[0] {
        for i := 1; i < len(strs); i++ {
            if  position > len(strs[i])-1 || letter != rune(strs[i][position]) {
                return strs[i][0:position]
            }
        }
    }
    return strs[0]
}
