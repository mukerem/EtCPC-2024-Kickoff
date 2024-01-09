def solve():
    n, k = map(int, input().split())

    if k:
        a = list(map(int, input().split()))
    else:
        a = []
        
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
    print(c)
    
solve()