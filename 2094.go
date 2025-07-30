// 2094. Finding 3-Digit Even Numbers
import "fmt"
import "sort"

func findEvenNumbers(digits []int) []int {
    // Use a map to avoid duplicate numbers
	resultMap := make(map[int]bool)
    var outputList []int
    for i:=0; i<len(digits); i++{
        for j:=0; j<len(digits); j++{
            for k:=0; k<len(digits); k++{
                //check for leading zeroes, odd endings at k, and cases where all inputs are odd
                if (i==j||j==k||i==k||(!isEven(digits[k])) || (digits[i] == 0) || (!isEven(digits[i]) && (!isEven(digits[j])) && (!isEven(digits[k])))){
                    continue
                }else{
                    number := digits[i]*100 + digits[j]*10 + digits[k]
                    resultMap[number] = true // Store number in map (duplicates are automatically handled)
                }
            }
        }
    }
	for number := range resultMap {
		outputList = append(outputList, number)
	}
	sort.Ints(outputList)
	return outputList
}

func isEven(number int)bool{
    if (number%2==0){
        return true
    }
    return false
}
