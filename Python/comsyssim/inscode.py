import sys

instype = {bytes([1]) : "mov",
           bytes([2]) : "add",
           bytes([3]) : "sub"
}

print(instype[bytes([1])])

print("Hello, World!", file=sys.stderr)
