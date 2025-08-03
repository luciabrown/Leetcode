// 70. Climbing Stairs

// Recursive Approach (Time Limit Exceeded)
func climbStairs(n int) int {
    if n <= 2 {
        return n
    }
    return climbStairs(n-1) + climbStairs(n-2)
}

// Manual For Loop Approach (Accepted)
func climbStairs(n int) int {
    if n <= 2 {
        return n
    }
    a, b := 1, 2
    for i := 3; i <= n; i++ {
        a, b = b, a+b
    }
    return b
}
