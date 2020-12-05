valid_count = 0

def parse_line_1(line):
    # lines look like 5-11 t: glhbttzvzttkdx\n
    global valid_count
    lim, letter, pwd = line.split(" ")
    letter = letter.replace(":", "")
    min_count, max_count = [int(pair) for pair in lim.split("-")]
    if (min_count <= pwd.count(letter) <= max_count):
        valid_count += 1

def parse_line(line):
    # lines look like 5-11 t: glhbttzvzttkdx\n
    global valid_count
    lim, letter, pwd = line.split(" ")
    letter = letter.replace(":", "")
    idx_1, idx_2 = [int(pair) - 1 for pair in lim.split("-")]
    
    if pwd[idx_1] == letter:
        if pwd[idx_2] != letter:
            valid_count += 1

    if pwd[idx_2] == letter:
        if pwd[idx_1] != letter:
            valid_count += 1

if __name__ == "__main__":
    with open("input2.txt","r") as f:
        lines = [line.strip() for line in f.readlines()]
        for line in lines:
            parse_line(line)
    print(f"Valid Passwords: {valid_count}")

