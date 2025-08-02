// 26. Remove Duplicates from Sorted Array

func removeDuplicates(nums []int) int {
        for i:=0; i<len(nums)-1;i=i{
            if nums[i] == nums[i+1]{
                nums = append(nums[:i], nums[i+1:]...)
            }else{
                i++
            }
        }
        return len(nums)
    }
