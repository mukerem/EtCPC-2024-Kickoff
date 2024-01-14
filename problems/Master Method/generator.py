import os
import random

def solve(a, b, k):
    x = b ** k
    if a > x:
        return "Case 1"
    elif a == x:
        return "Case 2"
    else:
        return "Case 3"
    
# Create a folder for test cases
os.makedirs("testcases", exist_ok=True)

def generate(i, t, a1, a2, b1, b2, k1, k2):
    with open(f"testcases/{i}.in", "w") as infile, open(f"testcases/{i}.out", "w") as outfile:
        # Generate random test data with different scenarios
        infile.write(f"{t}\n")

        for _ in range(t):
            a = random.randint(a1, a2)
            b = random.randint(b1, b2)
            k = random.randint(k1, k2)

            if random.random() < 0.2 and b ** k <= 1e18:
                a = b ** k

            # Calculate the result based on the problem description
            result = solve(a, b, k)

            # Write input and output to files
            infile.write(f"{a} {b} {k}\n")

            # Write output to file
            outfile.write(f"{result}\n")

for i in range(1, 11):
    t = random.randint(1, int(1e2))
    generate(i, t, 1, int(1e4), 2, 8, 1, 10)

for i in range(11, 21):
    t = random.randint(1000, int(1e4))
    generate(i, t, 1, int(1e12), 5, 10, 4, 18)

for i in range(21, 31):
    t = random.randint(int(9e4), int(1e5))
    generate(i, t, int(1e12), int(1e18), 10, 32, 10, 18)

print("30 test cases created in the 'testcases' folder.")