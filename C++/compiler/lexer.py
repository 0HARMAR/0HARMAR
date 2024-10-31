import json
tokens = []


with open(r'C:\Just-For-Fun\C++\compiler\add.k') as src:
    for line in src:
        if line == '\n': # is empty line
            continue
        tokens.append(line.rstrip('\n').split(" "))
    with open(r"C:\Just-For-Fun\C++\compiler\go_used\tokens.json",'w') as tkjs:
        json.dump(tokens,tkjs,indent=4)
    print("\n".join(tokens))
        