#Problem 18
import math  

# Step 1: Store the triangle as a 2D list
triangle = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
]

# Step 2: Start from the SECOND LAST row and move upward
# Why second last? Because the last row has no children
for i in range(len(triangle) - 2, -1, -1):
    
    # Step 3: Traverse each element in the current row
    for j in range(len(triangle[i])):
        
        # Step 4: For each element, choose the BEST path from below
        # It has two children:
        #   triangle[i+1][j]     -> left child
        #   triangle[i+1][j+1]   -> right child
        
        # We take the maximum of these two children
        best_child = max(triangle[i+1][j], triangle[i+1][j+1])
        
        # Add that best child value to current element
        # This means: "Best possible sum starting from this position"
        triangle[i][j] += best_child

# Step 5: After processing entire triangle,
# the top element contains the maximum path sum
print("Maximum total:", triangle[0][0])