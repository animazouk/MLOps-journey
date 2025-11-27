
'''
Practice Script 1: grid_analyzer.py (2D Lists + Nested Loops)
What to Build:

Create a 3x3 grid of numbers (e.g., 1–9).
Use nested loops to print each row as "Sum: <sum of row>".
Find and print the max value in the grid.
Handle if grid is empty (print "No data").

Hint:
grid = [[1,2,3], [4,5,6], [7,8,9]]
for row in grid:
print(f"Sum: {sum(row)}")
max_value = max(max(row) for row in grid)
Test: Run and see sums + max.
'''

def main():
    grid = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    try:
        if not grid:
            raise ValueError("Empty Grid")
        for row in grid:
            print(f" Sum of {grid.index(row) + 1} = {sum(row)}")
        
        max_value =  max(max(row) for row in grid)
        print(f" max value of the grid is {max_value}")
            
        max_value =  max(sum(row) for row in grid)
        print(f" max value of the grid is {max_value}")
    except ValueError:
        print("No data")
    
if __name__ == "__main__":
    main()


