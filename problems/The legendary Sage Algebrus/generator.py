import os
import random

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

def solve(a, b, c, d, e, f):
    x = solution1(a, b, c, d, e, f) + solution2(a, b, c, d, e, f) + solution3(a, b, c, d, e, f)
    x = set(x)
    if x:
        return sum(x)
    else:
        return "No Solution"

    
# Create a folder for test cases
os.makedirs("testcases", exist_ok=True)


def generate_non_zero_number(min_val, max_val):
    """
    Generate a random number between min_val and max_val, excluding 0.

    :param min_val: Minimum value of the range.
    :param max_val: Maximum value of the range.
    :return: A random non-zero integer within the given range.
    """
    number = 0
    while number == 0:
        number = random.randint(min_val, max_val)
    return number

def generate(i, t, a2, b2, c2, d2, e2, f2):
    with open(f"testcases/{i}.in", "w") as infile, open(f"testcases/{i}.out", "w") as outfile:
        # Generate random test data with different scenarios
        
        infile.write(f"{t}\n")

        for _ in range(t):
            a = generate_non_zero_number(-a2, a2)
            b = random.randint(-b2, b2)
            c = random.randint(-c2, c2)
            d = generate_non_zero_number(-d2, d2)
            e = random.randint(-e2, e2)
            f = random.randint(-f2, f2)

            rand = random.random()
            if rand < 0.05:
                x = random.randint(-1000, 1000)
                f = - (d * x ** 2 + e * x)
                c = - (a * x ** 2 + b * x)
            elif rand < 0.3:
                x = random.randint(-1000, 1000)
                f = - (d * x ** 2 + e * x)
            elif rand < 0.5:
                x = random.randint(-1000, 1000)
                c = 1 - (a * x ** 2 + b * x)
            elif rand < .7:
                x = random.randint(-1000, 1000)
                c = - 1 - (a * x ** 2 + b * x)
            
            # Write input to file
            infile.write(f"{a} {b} {c} {d} {e} {f}\n")
            
            # Calculate the result based on the problem description
            result = solve(a, b, c, d, e, f)

            # Write output to file
            outfile.write(f"{result}\n")

for i in range(1, 11):
    t = random.randint(1, int(1e2))
    generate(i, t, 5, 20, 100, 5, 20, 100)

for i in range(11, 21): 
    t = random.randint(int(1e2), int(1e5))   
    generate(i, t, 10, 100, 10000, 10, 100, 10000)

for i in range(21, 31):
    t = random.randint(int(9e4), int(1e5))   
    generate(i, t, 100, 1000, 1000000, 100, 1000, 1000000)

print("30 test cases created in the 'testcases' folder.")