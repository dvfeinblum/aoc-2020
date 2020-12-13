def compute_joltages(adapter_lst):
    # initialize counters and complete input
    one_jolt_diffs = 0
    three_jolt_diffs = 0
    adapter_lst.append(adapter_lst[-1] + 3)
    adapter_lst.insert(0,0)
    perm_lst = [0]*len(adapter_lst)

    for idx, joltage in enumerate(adapter_lst):

        if idx == 0:
            current_joltage = joltage
            perm_lst[idx] = 0
            continue

        choices = 0
        diff = joltage - current_joltage

        # look ahead to see if we have other choices
        if idx < len(adapter_lst) - 1 and adapter_lst[idx + 1] - current_joltage <= 3:
            choices += 1 
            perm_lst[idx+1] += 1
        if idx < len(adapter_lst) - 2 and adapter_lst[idx + 2] - current_joltage <= 3:
            choices += 1
            perm_lst[idx+2] += 1

        # calculate diffs
        if diff == 1:
            one_jolt_diffs += 1
        elif diff == 3:
            three_jolt_diffs += 1

        current_joltage = joltage
        perm_lst[idx] += choices + perm_lst[idx - 1]

    print(f"3 Jolt Diffs: {three_jolt_diffs}\n1 Jolt Diffs: {one_jolt_diffs}\nProduct: {one_jolt_diffs * three_jolt_diffs}")
    print(f"Choices: {perm_lst}")

if __name__ == "__main__":
    #with open("test10_little.txt", "r") as f:
    with open("test10.txt", "r") as f:
    #with open("input10.txt", "r") as f:
        outputs = [int(line) for line in f.readlines()]
    compute_joltages(sorted(outputs))
