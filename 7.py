from functools import reduce
import re

def parse_rules(rule_list):
    rule_dict = {}
    for rule in rule_list:
        if not rule:
            continue
        color, remainder = rule.split("s contain ")
        color = color.replace(" bag","")
        rule_dict[color] = {"sub_colors": set()}
        current_dict = rule_dict[color]
        for pred in remainder.replace(".","").replace("bags","bag").replace(" bag","").strip().split(","):
            m = re.match("(\d*) (.*)", pred.strip())
            if m:
                num, col = m.groups()
                col = col.strip()
                num = int(num.strip())
            else:
                col = "None"
                num = 0
            current_dict[col] = num
            current_dict["sub_colors"].add(col)

    return rule_dict

def recur_rules(parsed_rules):
    change = 1
    while change > 0:
        start_count = sum([len(x["sub_colors"]) for x in parsed_rules.values()])
        for color, rules in parsed_rules.items():
            for sub_color in rules["sub_colors"]:
                if sub_color in parsed_rules:
                    sub_color_dict = parsed_rules[sub_color]
                    multiplier = rules[sub_color]
                    for sub_sub_color in sub_color_dict["sub_colors"]:
                        rules[sub_sub_color] = sub_color_dict[sub_sub_color] * multiplier
                    rules["sub_colors"] = rules["sub_colors"].union(parsed_rules[sub_color]["sub_colors"])
        change = sum([len(x["sub_colors"]) for x in parsed_rules.values()]) - start_count
        print(f"Change after recurring: {change}")
    return parsed_rules

def find_gold_carriers(recurred_rules):
    gold_holders = 0
    for k, v in recurred_rules.items():
        if "shiny gold" in v["sub_colors"]:
            gold_holders += 1
            # print(f"A {k} bag can eventually hold a shiny gold bag!")

    return gold_holders

def count_total_bags(gold_dict):
    clean_dict = dict(gold_dict)
    del clean_dict["sub_colors"]
    del clean_dict["None"]
    return reduce(lambda memo,x: memo * x, [v for k,v in clean_dict.items()])

if __name__ == "__main__":
    with open("test7.txt","r") as f:
        raw_rules = f.read().split("\n")
    basic_rules = parse_rules(raw_rules)
    final_rules = recur_rules(basic_rules)
    print(f"{len(final_rules)} top-level rules")
    print(f"{find_gold_carriers(final_rules)} bag types can hold a shiny gold bag.")
    goldy_dict = final_rules['shiny gold']
    print(f"Gold Rules: {goldy_dict}")
    print(f"Note that there are {len(goldy_dict['sub_colors'])} sub colors and {len(goldy_dict) - 1} rule entries.")
    print(f"We need {count_total_bags(goldy_dict)} bags in our gold bag")
