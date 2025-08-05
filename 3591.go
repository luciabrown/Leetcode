// 3591. Check if Any Element Has Prime Frequency

func checkPrimeFrequency(nums []int) bool {
    freq := make(map[int]int)
    for _ , num :=  range nums {
        freq[num] = freq[num]+1
    }
    for _, value := range freq {
        if isPrime(value){
            return true
        }
    }
    return false
}

func isPrime(n int) bool{
    factors :=0
    for i:=1;i<=n;i++{
        if(n%i==0){
            factors++
        }
        if factors>2{
            return false
        }
    }
    return factors==2
}
