import os
import random
import string

def solve(arr):
    a = []
    for S, X, M, P, C, B, E in arr:
        score = 40 * X / 700 + 60 * (M * 2 + 1.5 * P + C + B + E) / 195
        score = round(score, 3)
        a.append((-score, S))
    a.sort()
    b = [(j, -i) for i, j in a]
    return b
    
# Create a folder for test cases
os.makedirs("testcases", exist_ok=True)

def generate(i, N, length):
    with open(f"testcases/{i}.in", "w") as infile, open(f"testcases/{i}.out", "w") as outfile:
        # Generate random test data with different scenarios
        infile.write(f"{N}\n")
        a = []

        for _ in range(N):
            S = ''.join(random.choices(string.ascii_uppercase, k=length))
            X = random.randint(0, 700)
            M = random.randint(0, 30)
            P = random.randint(0, 30)
            C = random.randint(0, 30)
            B = random.randint(0, 30)
            E = random.randint(0, 30)

            # Write input to file
            infile.write(f"{S} {X} {M} {P} {C} {B} {E}\n")

            # Write output to file
            a.append((S, X, M, P, C, B, E))
        
        # Calculate the result based on the problem description
        result = solve(a)

        # Write output to file
        for name, score in result:
            outfile.write(f"{name} {score:.3f}\n")

for i in range(1, 11):
    N = random.randint(1, int(1e3))
    generate(i, N, 5)

for i in range(11, 21):
    N = random.randint(int(1e3), int(1e5))
    generate(i, N, 5)

for i in range(21, 31):
    N = random.randint(int(9e4), int(1e5))
    generate(i, N, 10)

print("30 test cases created in the 'testcases' folder.")