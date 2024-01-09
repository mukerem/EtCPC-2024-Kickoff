from math import sqrt

def solution1(a, b, c, d, e, f):
    # ax^2 + bx + c = 1
    determinant = b * b - 4 * a * (c - 1)
    if determinant < 0:
        return []
    if determinant == 0:
        if b % (2 * a) == 0:
            return [-b // (2 * a)]
        return []
    
    root = int(determinant ** 0.5)
    if not  root * root == determinant:
        return []
    x1 = -b + root 
    x2 = -b - root

    x_sols = []
    if x1 % (2 * a) == 0:
        x_sols.append(x1 // (2 * a))
    if x2 % (2 * a) == 0:
        x_sols.append(x2 // (2 * a))
    return x_sols


def solution2(a, b, c, d, e, f):
    # ax^2 + bx + c = -1 and power even
    determinant = b * b - 4 * a * (c + 1)
    if determinant < 0:
        return []
    if determinant == 0:
        if b % (2 * a) == 0:
            x = -b // (2 * a)
            power = d * x ** 2 + e * x + f
            if power % 2 == 0:
                return [x]
        return []
    
    root = int(determinant ** 0.5)
    if not  root * root == determinant:
        return []
    x1 = -b + root 
    x2 = -b - root

    x_sols = []
    if x1 % (2 * a) == 0:
        x = x1 // (2 * a)
        power = d * x ** 2 + e * x + f
        if power % 2 == 0:
            x_sols.append(x)
    if x2 % (2 * a) == 0:
        x = x2 // (2 * a)
        power = d * x ** 2 + e * x + f
        if power % 2 == 0:
            x_sols.append(x)
        x_sols.append(x)
    return x_sols
    

def solution3(a, b, c, d, e, f):
    # ax^2 + bx + c = non zero and dx^2 + ex + f = 0
    determinant = e * e - 4 * d * f
    if determinant < 0:
        return []
    if determinant == 0:
        if e % (2 * d) == 0:
            x = -e // (2 * d)
            base = a * x ** 2 + b * x + c
            if base != 0:
                return [x]
        return []
    
    root = int(determinant ** 0.5)
    if not  root * root == determinant:
        return []
    x1 = -e + root
    x2 = -e - root

    x_sols = []
    if x1 % (2 * d) == 0:
        x = x1 // (2 * d)
        base = a * x ** 2 + b * x + c
        if base != 0:
            x_sols.append(x)
    if x2 % (2 * d) == 0:
        x = x2 // (2 * d)
        base = a * x ** 2 + b * x + c
        if base != 0:
            x_sols.append(x)
        x_sols.append(x)
    return x_sols

def solve():
    a, b, c, d, e, f = map(int, input().split())
    x = solution1(a, b, c, d, e, f) + solution2(a, b, c, d, e, f) + solution3(a, b, c, d, e, f)
    x = set(x)
    # print(x)
    if x:
        print(sum(x))
    else:
        print("No Solution")
    
for _ in range(int(input())):
    solve()