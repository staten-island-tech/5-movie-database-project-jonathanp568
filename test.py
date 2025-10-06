parking = input("How many parking spaces?")
parking = int(parking)
lane1 = input("Spaces in the first lane?")
lane2 = input("Spaces in the second lane?")
same = 0
num = 0
for i in range(parking):
    if lane1[num] and lane2[num] == "C":
        num += 1
        same += 1
    else:
        num += 1
print(same)


