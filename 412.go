// 412. Fizz Buzz
import (
    "strconv"
    "fmt"
)

func fizzBuzz(n int) []string {
    var outputList []string
    for i:=1;i<=n;i++{
        if (i%3==0 && i%5==0){
            outputList = append(outputList, "FizzBuzz")
        }else if (i%3==0){
            outputList = append(outputList, "Fizz")
        }else if (i%5==0){
            outputList = append(outputList,"Buzz")
        }else{
            outputList = append(outputList,strconv.Itoa(i))
        }
    }
    return outputList
}
