// 2413. Smallest Even Multiple

func smallestEvenMultiple(n int) int {
    result := n
    for i:=2;result%2!=0;i++{
        result=n*i
    }
    return result
}
