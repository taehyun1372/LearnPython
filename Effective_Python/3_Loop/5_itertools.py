import itertools

it = itertools.chain([1,2,3], [4,5,6])
print(list(it))

it2 = [1,2,3] + [4,5,6]
print(it2)

# it3 = itertools.chain(True, False)
# print(list(it3))

it4 = [i * 3 for i in ("a", "b", "c")]
it5 = [j * 3 for j in ("x", "y", "z")]
nested_it = [it4, it5]
print(nested_it)
print(list(itertools.chain.from_iterable(nested_it)))

it6 = itertools.chain("abc", "def")
print(list(it6))
it7 = itertools.chain.from_iterable(["abc", "def"])
print(list(it7))

it8 = itertools.repeat("hello", 3)
print(list(it8))

it9= itertools.cycle([1, 2])
result = [next(it9) for i in range(10)]
print(result)

def cycle_generator(cycle_list: list):
    count = 0
    while True:
        if count >= len(cycle_list):
            count = 0
            continue
        else:
            num = cycle_list[count]
            count+=1
            yield num

result = []
gen = cycle_generator([1,2,3])
for i in range(10):
    result.append(next(gen))

print(result)

it1, it2, it3 = itertools.tee(["first", "second"], 3)
print(list(it1))
print(list(it2))
print(list(it3))

keys = ["one", "two", "three"]
values = [1, 2]

normal = list(zip(keys, values))
print("zip: ", normal)

it = itertools.zip_longest(keys, values, fillvalue="nope")
longest = list(it)
print("zip_longest: ", longest)

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
first_five = itertools.islice(values, 5)
print("First five elements ", list(first_five))

middle_odd = itertools.islice(values, 0, 10, 2)
print("Middle odd elements ", list(middle_odd))

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
less_than_seven = lambda x: x < 7
it = itertools.takewhile(less_than_seven, values)
print(list(it))

it = itertools.dropwhile(less_than_seven, values)
print(list(it))

evens = lambda x: x % 2 == 0
filter_result = filter(evens, values)
print(list(filter_result))

filter_false_result = itertools.filterfalse(evens, values)
print(list(filter_false_result))

it = itertools.batched([1,2,3,4,5,6,7,8,9], 3)
print(list(it))

it = itertools.batched([1,2,3], 2)
print(list(it))

route = ["서울", "대전", "대구", "부산"]
it = itertools.pairwise(route)
print(list(it))

sum_reduce = itertools.accumulate(values)
print("Sum ", list(sum_reduce))

def modulo_20(first):
    return first % 20

# modulo_reduced = itertools.accumulate(values, modulo_20)
# print("Modulo ", list(modulo_reduced))

single = itertools.product([1, 2], repeat=2)
print("Signle ", list(single))

multitple = itertools.product([1,2], ["a", "b"], ["one", "two"])
print("Multiple ", list(multitple))

it = itertools.permutations([1, 2, 3, 4], 3)
print(list(it))

it = itertools.combinations([1, 2, 3, 4], 2)
print(list(it))

it = itertools.combinations_with_replacement([1, 2, 3, 4], 2)
print(list(it))
