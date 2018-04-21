import "fmt"
func longestCommonPrefix(strs []string) string {
        if len(strs) == 0 {
                return ""
        }
        prefix := strs[0]
        for _, word := range strs {
            for !strings.HasPrefix(word, prefix) {
                        prefix = prefix[0 : len(prefix)-1]
                        if prefix == "" {
                                return ""
                        }
                }

        }
        return prefix
}