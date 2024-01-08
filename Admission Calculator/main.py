def solve():
    N = int(input())
    a = []
    for _ in range(N):
        S, *Y = input().split()
        X, M, P, C, B, E = map(int, Y)
        score = 40 * X / 700 + 60 * (M * 2 + 1.5 * P + C + B + E) / 195
        score = round(score, 3)
        a.append((-score, S))
    a.sort()
    for i, j in a:
        print(j, -i)
        
solve()