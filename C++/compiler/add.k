int a = 1

int b = 2

b = a + b + b + a

int c = 10

c = b + a

int d = 20

c = d + c

int ret = calculate(c,d)

func calculate (int a,int b) int
    int sum = a + b + a
    return sum

func add (int op1,int op2) int
    int sum = op1 + op2
    return sum

int hmy = 111