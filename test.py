# def spaces(x,y):
#     occupied = 0
#     lane = 0
#     for char in x:
#         if x[lane] == "C" and y[lane] == "C":
#             occupied += 1
#             lane += 1
#         else:
#             lane += 1
#     print(occupied)
# spaces("C.CC.", "CCCCC")

def honi(x):
    list = 0
    list = int(list)
    num = 0
    for char in x:
        if x[list] == "H":
            list += 1
            num += 1
        else:
            list += 1
            if x[list] == "O":
                list += 1
                num += 1
            else:
                list += 1
                if x[list] == "N":
                    list += 1
                    num += 1
                else:
                    list += 1
                    if x[list] == "I":
                        list += 1
                        num += 1
                    else:
                        list += 1
    print(num)

honi("KHIEOANEIAJEHSOSANI")