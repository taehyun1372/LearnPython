car_ages = [0, 9, 4, 8, 7, 20, 19, 1, 6, 15]
car_ages_descending = sorted(car_ages, reverse=True)
print(car_ages_descending)
# oldest, second_oldest, = car_ages_descending
oldest = car_ages_descending[0]
second_oldest = car_ages_descending[1]
others = car_ages_descending[2:]
print(oldest, second_oldest, others)

oldest, second_oldest, *others = car_ages_descending
print(oldest, second_oldest, others)

*others, second_youngest, youngest = car_ages_descending
print(youngest, second_youngest, others)

car_invenetory = {
    "Downtown" : ("Silver Shadow", "Pinto", "DMC"),
    "Airport" : ("Skyline", "Viper", "Gremlin", "Nova")
}

((loc1, (best1, *rest1)), (loc2, (best2, *rest2))) = car_invenetory.items()
print(f"{loc1}, {best1}, {len(rest1)}")
print(f"{loc2}, {best2}, {len(rest2)}")

short_list = [1, 2]
first, second, *others = short_list
print(first, second, others)