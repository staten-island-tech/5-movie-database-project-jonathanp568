# parking = input("How many parking spaces?")
# parking = int(parking)
# lane1 = input("Spaces in the first lane?")
# lane2 = input("Spaces in the second lane?")
# same = 0
# num = 0
# for i in range(parking):
#     if lane1[num] and lane2[num] == "C":
#         num += 1
#         same += 1
#     else:
#         num += 1
# print(same)

def spaces(x,y):
    occupied = 0
    lane = 0
    for char in x:
        if x[lane] == "C" and y[lane] == "C":
            occupied += 1
            lane += 1
        else:
            lane += 1
    print(occupied)
spaces("C.CC.", "CCCCC")