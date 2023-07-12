N = int(input())
satan = 666
count_ = 0

while True:
    if '666' in str(satan):
        count_ += 1
    if count_ == N:
        print(satan)
        break

    satan += 1