import (
	"math"
)

func reverse(x int) int {
    xReversed := 0
    
    for x != 0 {
        xReversed = (xReversed * 10) + (x % 10)
        x = x / 10
    }

    if xReversed < math.MinInt32 || xReversed > math.MaxInt32 {
        return 0
    }
    return int(xReversed)
}