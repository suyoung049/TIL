import sys
sys.stdin = open("3_input.txt", "r")

jae = input()
doctor = input()

jae_a = 0
doctor_a = 0

for i in jae:
    if i == 'a':
        jae_a += 1

for k in doctor:
    if k == "a":
        doctor_a += 1

if jae_a >= doctor_a:
    print("go")
else:
    print("no")