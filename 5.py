# puzzle input looks like FBFBBFFRLR
# 128 rows, 8 cols
# F or L means you take lower half

import math

def find_seat(inp):
    row = 127
    row_start = 0
    col = 7
    col_start = 0

    for char in inp:
        delta = math.ceil((row - row_start) / 2)
        if char == "F":
            row -= delta
        elif char == "B":
            row_start += delta
        else:
            first_col = char
            break
        # print(f"New row bounds: {row_start} through {row}")

    col_steps = list(inp.split(first_col,1)[1])
    col_steps = [first_col] + col_steps

    for char in col_steps:
        delta = math.ceil((col - col_start) / 2)
        if char == "L":
            col -= delta
        elif char == "R":
            col_start += delta
        else:
            print("Something very odd happened")
            exit(1)
        # print(f"New col bounds: {col_start} through {col}")

    # print(f"Seat Row: {row}\nSeat Col: {col}\nSeat ID: {row * 8 + col}")
    return row * 8 + col

def determine_my_id(ids):
    expected_ids = set()
    for i in range(128):
        for j in range(8):
            curr_id = i * 8 + j
            if 48 <= curr_id <=922:
                expected_ids.add(i * 8 + j)
    print(f"Number of total IDs: {len(expected_ids)}")
    print(f"Seat ID Missing: {expected_ids - ids}")

if __name__ == "__main__":
    with open("input5.txt","r") as f:
        high_pass = 0
        low_pass = 1023
        seen_ids = set()
        for boarding_pass in f.readlines():
            pass_id = find_seat(boarding_pass.strip())
            high_pass = max(high_pass, pass_id)
            low_pass = min(low_pass, pass_id)
            seen_ids.add(pass_id)

    print(f"We ID'd {len(seen_ids)} seats.")
    determine_my_id(seen_ids)    

    print(f"Highest Seat ID: {high_pass}")
    print(f"Lowest Seat ID: {low_pass}")
