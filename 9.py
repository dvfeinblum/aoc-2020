def crack_xmas(vals, preamble_length):
    nums = vals[preamble_length:]
    idx = 0

    for num in nums:
        valid = False
        preamble = vals[idx:idx + preamble_length]
        for pre in preamble:
            diff = num - pre
            if diff in preamble:
                valid = True
                idx += 1
                break
        
        if not valid:
            print(f"{num} is not the sum of any values in the preamble.")
            return num

def find_weakness(vals, weakness):
    length = 0
    for idx, num in enumerate(vals):
        tot = num
        jdx = idx + 1
        small = num
        large = num
        while jdx < len(vals) and tot < weakness:
            new_val = vals[jdx]
            tot += new_val
            small = min(small, new_val)
            large = max(large, new_val)
            if tot == weakness and jdx - idx >= 2:
                print(f"Found the cont sum.\nMin val: {small}\nMax val: {large}\nSum: {small+large}")
                break
            jdx += 1

if __name__ == "__main__":
    with open("input9.txt", "r") as f:
        inps = [int(line) for line in f.readlines()]

    bad_val = crack_xmas(inps, 25)
    find_weakness(inps[25:], bad_val)
