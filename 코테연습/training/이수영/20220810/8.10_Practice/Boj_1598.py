N, M = map(int, input().split())

N = N -1
M = M -1

wid = abs((N //4) - (M//4))
vir = abs((N % 4) -(M % 4))

print(wid + vir)