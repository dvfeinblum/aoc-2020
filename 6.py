
def check_answers(ans):
    yes_ans = {}
    idx = 0
    for person in ans.split("\n"):
        if person == '':
            continue
        yes_ans[idx]=set(person)
        idx += 1
    # print(f"yes_ans: {yes_ans}")
    shared_ans = set.intersection(*yes_ans.values())
    # print(f"shared_ans: {shared_ans}")
    return len(shared_ans)

if __name__ == "__main__":
    with open("input6.txt","r") as f:
        ans_total = 0
        for blob in [line for line in f.read().split("\n\n")]:
            ans_total += check_answers(blob)

    print(f"Total Yes: {ans_total}")
