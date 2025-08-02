// 136. Single Number

import "slices"
func singleNumber(nums []int) int {
    uniqueSlice := []int{}
    var returnValue int
    returnValue =0
        for i:=0; i<len(nums);i=i{
            if !slices.Contains(uniqueSlice,nums[i]){
                uniqueSlice = append(uniqueSlice, nums[i])
                nums = append(nums[:i], nums[i+1:]...)
            }else{
                i++
            }
        }
        for j:=0; j<len(uniqueSlice);j++{
            if !slices.Contains(nums,uniqueSlice[j]){
                returnValue = uniqueSlice[j]
            }
        }
        return returnValue
    }
