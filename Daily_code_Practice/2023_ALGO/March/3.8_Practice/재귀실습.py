# def fact(n):
#     if n == 0:
#         return 1
#     return n*fact(n-1)

# f = fact(4)
# print(f)


# # 1부터 n까지 더하는 함수

# def sr(n):
#     if n == 1:
#         return 1
#     return n + sr(n-1)

# print(sr(10))

# 피보나치 수열

def fi(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    
    return fi(n-1) + fi(n-2)

print(fi(10))