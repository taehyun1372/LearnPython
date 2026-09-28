def my_func(**kwargs):
    for key, value in kwargs.items():
        print("%s = %s" %(key, value))

my_func(goose="gosling", kangaroo="joey")

class MyClass:
    def __init__(self):
        self.alligator = "hatchling"
        self.elephant = "calf"

a = MyClass()
for key, value  in a.__dict__.items():
    print(f"key  : {key}, value : {value}")

votes = {
    "cat" : 1281,
    "dog" : 587,
    "rabbit" : 863
}

def populate_ranks(votes, ranks):
    sorted_votes = sorted(list(votes.values()))
    for i, vote in enumerate(sorted_votes):
        for key, value in votes.items():
            if value == vote:
                ranks[key] = i + 1
    return ranks

ranks = {}
populate_ranks(votes, ranks)
print(ranks)

def get_winnder(ranks):
    return next(iter(ranks))

winner = get_winnder(ranks)
print(winner)

winner = get_winnder(ranks)
print(winner)

counters = {
    "Milky" : 2,
    "Sauer" : 1
}

key = "Whit"

# if key in counters:
#     count = counters[key]
# else:
#     count = 0

# try:
#     count = counters[key]
# except Exception as ex:
#     print("Exception occured ", ex)
#     count = 0

# counters[key] = count + 1

count = counters.get(key, 0)
counters[key] = count + 1

print(counters)

votes = {
    "Milky" : ["Roy", "Kate"],
    "Souer" : ["Charle", "Buffet"],
}

key = "Whit"
who = "Victoria"

# if key in votes:
#     names = votes[key]
# else:
#     votes[key] = names = []

# try:
#     names = votes[key]
# except Exception as e:
#     print(e)
#     votes[key] = names = []

names = votes.get(key)
if names is None:
    votes[key] = names = []

names.append(who)
print(votes)

pictures = {}
path = "profile_1234.png"

if (hanle := pictures.get(path)) is None:
    try:
        handle = open(path, "a+b")
    except OSError:
        print("Cannot open the file ", path)
    else:
        pictures[path] = handle

handle.seek(0)
image_data = handle.read()