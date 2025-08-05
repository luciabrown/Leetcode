// 3477. Fruits Into Baskets II

func numOfUnplacedFruits(fruits []int, baskets []int) int {
    return len(placeFruit(fruits, baskets))
}

func placeFruit(fruits []int, baskets []int) []int {
    fruitIndex := 0
    for fruitIndex < len(fruits) {
        placed := false
        basketIndex := 0
        for basketIndex < len(baskets) {
            if fruits[fruitIndex] <= baskets[basketIndex] {
                fruits = append(fruits[:fruitIndex], fruits[fruitIndex+1:]...)
                baskets = append(baskets[:basketIndex], baskets[basketIndex+1:]...)
                placed = true
                break // Move to next fruit
            } else {
                basketIndex++ // Move to next basket
            }
        }
        if !placed {
            // All baskets were tried
            fruitIndex++
        }
    }
    return fruits
}
