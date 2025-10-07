import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)
list = 0
list = int(list)
for i in range(14117):
    print(data[list]["title"])
    list += 1