import sys
input = sys.stdin.readline

def solve():
    T = int(input())
    for _ in range(T):
        x1, y1, r1, x2, y2, r2 = map(int, input().split())
        dx = x1 - x2
        dy = y1 - y2
        d_sq = dx*dx + dy*dy
        sum_r = r1 + r2
        diff_r = abs(r1 - r2)

        # 두 원이 완전히 일치할 때
        if d_sq == 0 and r1 == r2:
            print(-1)
        # 만나지 않거나 한 원이 다른 원 안에 완전히 있을 때
        elif d_sq > sum_r*sum_r or d_sq < diff_r*diff_r:
            print(0)
        # 외접하거나 내접할 때
        elif d_sq == sum_r*sum_r or d_sq == diff_r*diff_r:
            print(1)
        # 두 점에서 만날 때
        else:
            print(2)

if __name__ == "__main__":
    solve()
