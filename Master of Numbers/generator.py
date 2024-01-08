import os
import random

def solve(N):
    n = int(N ** .5)
    result = n * (n + 1) * (2 * n + 1) // 6
    return result
    
# Create a folder for test cases
os.makedirs("testcases", exist_ok=True)

def generate(i, t, N1, N2):
    with open(f"testcases/{i}.in", "w") as infile, open(f"testcases/{i}.out", "w") as outfile:
        # Generate random test data with different scenarios
        infile.write(f"{t}\n")

        for _ in range(t):
            N = random.randint(N1, N2)
            
            # Calculate the result based on the problem description
            result = solve(N)

            # Write input to file
            infile.write(f"{N}\n")

            # Write output to file
            outfile.write(f"{result}\n")

for i in range(1, 11):
    t = random.randint(1, int(1e2))
    generate(i, t, 1, int(1e5))

for i in range(11, 21):
    t = random.randint(1000, int(1e4))
    generate(i, t, int(1e5), int(1e12))

for i in range(21, 31):
    t = random.randint(int(9e4), int(1e5))
    generate(i, t, int(1e10), int(1e12))

print("30 test cases created in the 'testcases' folder.")