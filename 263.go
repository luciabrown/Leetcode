// 263. Ugly Number

import "slices"
import "math"
import "fmt"
func isUgly(n int) bool {
    if n<=0{
        return false
    }
    checkThisList := primeFactors(n)
    valid := []int{2,3,5}
    if len(checkThisList) ==0{
        return true
    }
    if !slices.Contains(valid, checkThisList[len(checkThisList)-1]){
        return false
    }
    return true
}

func primeFactors(n int) []int{
    primeList:=[]int{}

    for n%2==0{
        if !slices.Contains(primeList, 2){
            primeList = append(primeList, 2)
        }
        n=n/2
    }

    for i:=3; i<=(int(math.Sqrt(float64(n)))); i=i+2{
        for n%i==0{
            if !slices.Contains(primeList, i){
                primeList = append(primeList, i)
            }
            n=n/i
        }
    }
    if n>2{
        primeList = append(primeList, n)
    }
    return primeList
}
