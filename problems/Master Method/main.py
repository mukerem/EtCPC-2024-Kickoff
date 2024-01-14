def solve():
    a, b, k = map(int, input().split())
    x = b ** k
    if a > x:
        print("Case 1")
    elif a == x:
        print("Case 2")
    else:
        print("Case 3")

for _ in range(int(input())):
    solve()