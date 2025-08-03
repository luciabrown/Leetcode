// 20. Valid Parentheses

func isValid(s string) bool {
    stack := &Stack{}
    for i:=0;i<len(s);i++{
        switch rune(s[i]){
            case '(','{','[':
                stack.Push(rune(s[i]))
            case ')':
                if stack.Peek() == '('{
                    stack.Pop()
                }else{
                    return false
                }
            case '}':
                if stack.Peek() == '{'{
                    stack.Pop()
                }else{
                    return false
                }
            case ']':
                if stack.Peek() == '['{
                    stack.Pop()
                }else{
                    return false
                }
        }
    }
    if stack.isEmpty(){
        return true
    }
    return false
}

// Stack structure
type Stack struct{
    brackets[]rune
}

// Push
func (stack *Stack) Push(char rune) {
	stack.brackets = append(stack.brackets, char)
}

// Pop
func (stack *Stack) Pop() (rune) {
	if len(stack.brackets) == 0 {
		return 0 // stack is empty
	}
	top := stack.brackets[len(stack.brackets)-1] // get top of stack
	stack.brackets = stack.brackets[:len(stack.brackets)-1]
	return top
}

// Peek
func (stack *Stack) Peek() (rune) {
	if len(stack.brackets) == 0 {
		return 0
	}
	return stack.brackets[len(stack.brackets)-1]
}

// IsEmpty
func (stack *Stack) isEmpty() bool {
	return len(stack.brackets) == 0
}
