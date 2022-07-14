def are(a, b):

    return a * b

def rou(a, b):

    return (a+b) * 2

result = (are(20, 30), rou(20, 30))

print(result)

# 강사님 풀이 
def rectangle(a, b): 
    area = a * b
    perimeter = 2 * (a+b)
    return area, perimeter

print(rectangle(20, 30))