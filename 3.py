DEBUG = False

def parse_map(raw_map):
    # a raw row looks like .........#.#.#.........#.#.....
    return [list(line.strip()) for line in raw_map]
    

def count_trees_1(slope_map, x_delta, y_delta):
    tree_count = 0
    x = 0
    y = 0
    height = len(slope_map) - 1
    width = len(slope_map[0]) - 1
    while y < height:
        x += x_delta
        y += y_delta
        if DEBUG:
            print(f"Line ({x}, {y}): {slope_map[y]}")
            print(f"Adjusted x: {x % (width + 1)}")
        if slope_map[y][x % (width + 1)] == "#":
            if DEBUG:
                print("Hit a tree")
            tree_count += 1

    print(f"We hit {tree_count} trees.")
    return tree_count

if __name__ == "__main__":
    with open("input3.txt", "r") as f:
        parsed_map = parse_map(f.readlines())
        slopes = [
            [1,1],
            [3,1],
            [5,1],
            [7,1],
            [1,2]
        ]
        product = 1
        for slope in slopes:
            product *= count_trees_1(parsed_map, *slope)

    print(f"Product of Hit Trees: {product}")
