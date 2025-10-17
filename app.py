import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

# list = 0
# for i in range(14117):
#     print(data[list]["title"])
#     list += 1

# list = 0
# prompt = input("Movies after ____")
# prompt = int(prompt)
# while list != 14117:
#     if data[list]["year"] > prompt:
#         print(data[list]["title"])
#         list += 1
#     else: 
#         list += 1

# list = 14116
# prompt = input("Movies before ____")
# prompt = int(prompt)
# while list != -1:
#     if data[list]["year"] < prompt:
#         print(data[list]["title"])
#         list -= 1
#     else: 
#         list -= 1

# list = 0
# prompt = input("Movies during ____")
# prompt = int(prompt)
# while list != 14117:
#     if data[list]["year"] == prompt:
#         print(data[list]["title"])
#         list += 1
#     else: 
#         list += 1

# list = 0
# prompt = input("Search for a movie")
# while list != 14117:
#     if prompt == data[list]["title"]:
#         print(data[list])
#         break
#     else:
#         list += 1


prompt = input("Movie genre:")
list = 0
for i in data:
    if prompt in data[list]["genres"]:
        print(data[list]["title"])
        list += 1
    else:
        list += 1