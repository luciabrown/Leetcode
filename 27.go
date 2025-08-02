// 27. Remove Element

func removeElement(nums []int, val int) int {
    // If empty slice
    if len(nums)==0{
        return 0
    }
    for i:=0; i<len(nums)-1;i=i{
        if nums[i] == val{
            nums = append(nums[:i], nums[i+1:]...)
        }else{
            i++
        }
    }
    // Last element out of bounds in For loop
    if nums[len(nums)-1] == val{
        nums = nums[:len(nums)-1]
    }
    return len(nums)
}
