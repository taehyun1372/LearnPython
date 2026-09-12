no_snack = ()
snack = ("chip",)
print(snack[0])

snack_calories = {
    "potato": 140,
    "popcorn": 80,
    "peanut": 190
}

items = list(snack_calories.items())
print(items)
print(type(items))

item = ("호박엿", "식혜")
first_item = item[0]
first_half = item[:1]
print(first_item)
print(first_half)

pair = ("약과", "호박엿")
# pair[0] = "타래과"

item = ("호박엿", "식혜")
first, second = item
print(first, " and ", second)

favorite_snacks = {
    "짭조름한 과자" : ("프레즐", 100),
    "달콤한 과자": ("쿠키", 180),
    "채소": ("당근", 20)
}

((type1, (name1, cals1)),
(type2, (name2, cals2)),
(type3, (name3, cals3))) = favorite_snacks.items()

print(f"{type1}, {name1}, {cals1}")
print(f"{type2}, {name2}, {cals2}")
print(f"{type3}, {name3}, {cals3}")

def bubble_sort(a):
    for _ in range(len(a)):
        for i in range(1, len(a)):
            if a[i] < a[i-1]:
                temp = a[i]
                a[i] = a[i-1]
                a[i-1] = temp

def bubble_sort2(a):
    for _ in range(len(a)):
        for i in range(1, len(a)):
            if a[i] < a[i-1]:
                a[i], a[i-1] = a[i-1], a[i]

names = ["프레즐", "당근", "쑥갓", "베이컨"]
bubble_sort2(names)
print(names)

snacks = [("베이컨", 350), ("도넛", 240), ("머핀", 190)]
for rank, (item, cals) in enumerate(snacks, start=1):
    print(f"{rank}, {item}, {cals}")
    