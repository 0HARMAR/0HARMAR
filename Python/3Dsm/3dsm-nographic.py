point1 = (1,2,3)

point2 = (2,1,4)

point3 = (3,3,3)

def p3():
    print(point3)
    p1()

def p2():
    print(point2)
    p3()
    
def p1():
    print(point1)
    p2()


def start():
    p1()
    
start()