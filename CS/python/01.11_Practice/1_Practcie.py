java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

print(java.intersection(python))

print(java.union(python))

print(java.difference(python))

from random import*
users = list(range(1, 21))

shuffle(users)

winners = sample(users, 4)

