import json
import sys

tokens = []
path = ""

if __name__ == "__main__":
    path = sys.argv[1]

print(path)
with open(path) as src:
    for line in src:
        if line == '\n': # is empty line
            continue
        elif line.startswith('    '):
            token = line.rstrip('\n').split()
            token.insert(0,'\t')
            tokens.append(token)
            continue
        elif line.startswith('func'):
            token = line.rstrip('\n').split()
            to_fix = []
            for index,token_ in enumerate(token):
                if ',' in token_:
                    splited = token_.split(',')
                    to_fix.append((index,splited))
            for element in to_fix:
                index = element[0]
                splited = element[1]
                del token[index]
                token.insert(index,splited[0])
                token.insert(index+1,splited[1])
            tokens.append(token)
            continue

        tokens.append(line.rstrip('\n').split())
    with open(r"C:\Just-For-Fun\C++\compiler\go_used\tokens.json",'w') as tkjs:
        json.dump(tokens,tkjs,indent=4)
    print("\n".join(str(token) for token in tokens))

        