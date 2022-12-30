my_set = {1,2,3,4,3,3,3,3}

print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합
print(java & python)
print(java.intersection(python))

# 합집합
print(java|python)
print(java.union(python))

# 차집합
print(java-python)
print(java.difference(python))
print(python.difference(java))

