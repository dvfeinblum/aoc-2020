import re
expected_keys = {
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    "cid"
}

def height_checker(raw_hgt):
    if "in" in raw_hgt:
        hgt = int(raw_hgt.split("in")[0])
        return 59 <= hgt <= 76
    elif "cm" in raw_hgt:
        hgt = int(raw_hgt.split("cm")[0])
        return 150 <= hgt <= 193
    else:
        return False

expected_values = {
    "byr": lambda x: 1920 <= int(x) <= 2002,
    "iyr": lambda x: 2010 <= int(x) <= 2020,
    "eyr": lambda x: 2020 <= int(x) <= 2030,
    "hgt": height_checker,
    "hcl": lambda x: re.search("^#[a-f0-9]{6}$", x) is not None,
    "ecl": lambda x: x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": lambda x: re.search("^\d{9}$", x) is not None,
    "cid": lambda x: True
}


def parse_pp_1(raw_pass):
    entries = re.split(" |\n", raw_pass)
    keys = set([entry.split(":")[0] for entry in entries])
    keys.add("cid")
    if keys == expected_keys:
        return 1
    else:
        return 0

def parse_pp(raw_pass):
    entries = re.split(" |\n", raw_pass)
    try:
        entries.remove("")
    except:
        pass
    pp_dict = {key:value for (key,value) in [entry.split(":") for entry in entries]}
    pp_dict["cid"] = "foo"
    if set(pp_dict.keys()) != expected_keys:
        return 0
    for k,v in pp_dict.items():
        if not expected_values[k](v):
            return 0

    return 1


if __name__ == "__main__":
    with open("input4.txt", "r") as f:
        raw = f.read()
        raw_passes = raw.split("\n\n")
        print(f"Number of passports to scan: {len(raw_passes)}")
        valid_count = 0
        for passport in raw_passes:
            valid_count += parse_pp(passport)

    print(f"Valid Passports: {valid_count}")
