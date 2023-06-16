import sys
sys.stdin = open("1_input.txt", "r")
input = sys.stdin.readline

n = int(input())
k = int(input())

if k >= n:
    print(0)

else:
    sensor = list(map(int, input().split()))

    sensor.sort()

    distance = []
    for i in range(n-1):
        if sensor[i] != sensor[i+1]:
            distance.append(sensor[i+1] - sensor[i])

    distance.sort()

    for _ in range(k-1):
        distance.pop()

    print(sum(distance))

