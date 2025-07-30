//414. Third Maximum Number

import "slices"
import "sort"

func thirdMax(nums []int) int {
    seenItem := make(map[int]bool)
    removedDuplicates := []int{}
    holdOriginalMax := slices.Max(nums)
    for _,item := range nums{
        if !seenItem[item]{
            seenItem[item] = true
            removedDuplicates = append(removedDuplicates,item)
        }
    }
    if len(removedDuplicates) < 3{
        return holdOriginalMax
    }
    sort.Ints(removedDuplicates)
    return removedDuplicates[len(removedDuplicates)-3]
}
