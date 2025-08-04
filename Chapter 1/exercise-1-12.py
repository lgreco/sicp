def pascal_recursive(row, col):
    if col == 0 or col == row:
        # The first and last column in every row is 1
        return 1
    # The remaining columns in a row are the sum of the rows above them
    return pascal_recursive(row-1, col-1)+pascal_recursive(row-1,col)

def build_pascal_triangle(rows):
    """TODO: centered printing."""
    for row in range(rows):
        for col in range(row+1):
            print(f"{pascal_recursive(row, col):5d}", end =" ")
        print()

build_pascal_triangle(5)