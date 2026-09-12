fresh_fruit = {
    "사과": 10,
    "바나나": 1,
    "레몬": 5
}

def make_lemonade(count):
    print(f"Made lemonade..{count}")

def out_of_stock():
    print("Lemon is out of stock")

# count = fresh_fruit.get("레몬", 0)
# if count:
#     make_lemonade(count)
# else:
#     out_of_stock()

if count:= fresh_fruit.get("레몬", 0):
    make_lemonade(count)
else:
    out_of_stock()
print(count)

count = fresh_fruit.get("바나나", 0)

if count >= 2:
    print("offer banana")
else:
    count = fresh_fruit.get("사과", 0)
    if count >=4:
        print("offer apple")
    else:
        count = fresh_fruit.get("레몬", 0)
        if count >=1:
            print("offer lemon")
        else:
            print("We cannot provide any..")

if (count:=fresh_fruit.get("바나나")) >= 2:
    print("offer banana")
elif (count:=fresh_fruit.get("사과")) >= 4:
    print("offer apple")
elif (count:=fresh_fruit.get("레몬")) >= 1:
    print("offer lemon")

def pick_fruit():
    return "사과", 10

def make_juice(fruit, count):
    return "사과쥬스", 10

bottles = {}
# fresh_fruit = pick_fruit()
# i = 0
# while fresh_fruit:
#     i += 1
#     if i > 10:
#         break
#     fruit, count = fresh_fruit
#     batch = make_juice(fruit, count)
#     bottles[batch[0]] = bottles.get(batch[0], 0) + batch[1]
#     fresh_fruit = pick_fruit()

while fresh_fruit := pick_fruit():
    i += 1
    if i > 10:
        break
    fruit, count = fresh_fruit
    batch = make_juice(fruit, count)
    bottles[batch[0]] = bottles.get(batch[0], 0) + batch[1]

print(bottles)
