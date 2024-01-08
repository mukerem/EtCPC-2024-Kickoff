import os
import random

def solve(n, k, a):
    
    final = [0] * (n+1)
    current = [0] * (n+1)
    for i in a:
        final[i] = 1
    
    c = 0
    for i in range(1, n+1):
        if final[i] == current[i]:
            continue
        c += 1
        for j in range(i, n + 1, i):
            current[j] = 0 if current[j] else 1
    return c
    
    
# Create a folder for test cases
os.makedirs("testcases", exist_ok=True)

def generate(i, n1, n2, k1):
    with open(f"testcases/{i}.in", "w") as infile, open(f"testcases/{i}.out", "w") as outfile:
        # Generate random test data with different scenarios
        
        n = random.randint(n1, n2)
        k = random.randint(k1, n)
        infile.write(f"{n} {k}\n")

        a = random.sample(range(1, n + 1), k)
        
        # Write input to file
        infile.write(" ".join(map(str, a)))
        
        # Calculate the result based on the problem description
        result = solve(n, k, a)

        # Write output to file
        outfile.write(f"{result}\n")

for i in range(1, 11):
    generate(i, 1, int(1e3), 1)

for i in range(11, 21):    
    generate(i, int(1e3), int(1e5), int(1e3))

for i in range(21, 31):
    generate(i, int(9e4), int(1e5), int(1e4))

print("30 test cases created in the 'testcases' folder.")