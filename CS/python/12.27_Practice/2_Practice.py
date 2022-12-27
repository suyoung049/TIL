# subway1 = 10
# subway2 = 20
# subway3 = 30

# subway = [10, 20, 30]


subway = ["유재석", "조세호", "박명수"]


print(subway.index("조세호"))

subway.append("하하")

subway.insert(1, "정형돈")

subway.append("유재석")

print(subway.count("유재석"))

num_list = [5,2,4,1]

num_list.sort(reverse=True)


print(num_list)

mix_list = ["조세호", 3, True]

num_list.extend(mix_list)

print(num_list)