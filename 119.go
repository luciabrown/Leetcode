// 119. Pascal's Triangle II

func getRow(rowIndex int) []int {
    if rowIndex == 0{
        return []int{1} // Handler for 0th row
    }
    triangle := generate(rowIndex+1)  // Create a triangle with the rowIndex
    return triangle[len(triangle)-1]    // Return last row of the generated triangle
}


// Solution From 118. Pascal's Triangle
func generate(numRows int) [][]int {
	nodeLevels := BuildPascalTree(1, numRows) 
	result := make([][]int, len(nodeLevels))   // initialise 2D slice

	for i, level := range nodeLevels {
		row := make([]int, len(level))      // length of the level
		for j, node := range level {
			row[j] = node.Value             // populate level with values
		}
		result[i] = row
	}
	return result 
}

// Node structure
type Node struct {
	Value int
	Left  *Node
	Right *Node
}

func BuildPascalTree(rootVal int, N int) [][]*Node {
	if N <= 0 {
		return [][]*Node{}
	}
	// Initialize first level with root
	root := &Node{Value: rootVal}
	levels := [][]*Node{{root}}

	for level := 1; level < N; level++ {
		prev := levels[level-1]
		curr := make([]*Node, 0, level+1)
		for i := 0; i <= level; i++ {
			var val int
			// Left edge (only one parent)
			if i == 0 {
				val = prev[0].Value
			// Right edge (only one parent)
			} else if i == level {
				val = prev[len(prev)-1].Value
			// Middle (sum of two parents)
			} else {
				val = prev[i-1].Value + prev[i].Value
			}
			curr = append(curr, &Node{Value: val})
		}
		levels = append(levels, curr)
	}
	return levels
}
