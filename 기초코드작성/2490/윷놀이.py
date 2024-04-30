yoot = {3: "A", 2:"B", 1:"C", 0:"D", 4:"E"}

for i in range(3):
    yoot_info = list(map(int, input().split()))
    print(yoot[yoot_info.count(1)])