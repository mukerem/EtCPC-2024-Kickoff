def solve():
    N = int(input())
    n = int(N ** .5)
    result = n * (n + 1) * (2 * n + 1) // 6
    print(result)

for _ in range(int(input())):
    solve()