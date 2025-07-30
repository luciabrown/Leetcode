//1317. Convert Integer to the Sum of Two No-Zero Integers
import "strconv"
import "strings"

func getNoZeroIntegers(n int) []int {
    var outputList []int
    a:=n/2
    b:=n/2
    if(n%2!=0){
        b= n-a
    }
    if(!(strings.Contains(strconv.Itoa(a),"0")) && !(strings.Contains(strconv.Itoa(b),"0"))){
            outputList = append(outputList,a,b)
            return outputList
    }else{
        for(a>0 && b<n) {
            a=a-1
            b++
            if(!(strings.Contains(strconv.Itoa(a),"0")) && !(strings.Contains(strconv.Itoa(b),"0"))){
            outputList = append(outputList,a,b)
            return outputList
            }   
        }
    }
    return outputList
}
