import string
import sys

slayer = ["버피", "앤", "아스틴"]
print(" ".join(slayer))

print(" ".join(reversed(slayer)))

name = "스칼렛"
print(name.ljust(50, "-"))
print(name.rjust(50, "-"))

print("{} {} {}".format("파이선", "자료구조", "알고리즘"))

word = "Hello"
char_list = [*word]
print(char_list)
char_tuple = (*word,)
print(char_tuple)

slayers = "로미오\n줄리엣"
print(slayers.splitlines())

slayers = "버피*크리스-메리*16"
fields = slayers.split("*")
print(fields)
job = fields[1].split("-")
print(job)

slayers = "로미오 & 줄리엣999"
print(slayers.strip("999"))

def count_unique_word():
    words = {}
    strip = string.whitespace + string.punctuation + string.digits + "\"'"
    for filename in sys.argv[1:]:
        with open(filename) as file:
            for line in file:
                print(line)
    #             for word in line.lower().split():
    #                 word = word.strip(strip)
    #                 if len(word) > 2:
    #                     words[word] = words.get(word, 0) + 1
    #
    # for word in sorted(words):
    #     print(word, words[word])

def alphabetical_sorting(items :list, key : string):
    items = list(set(items))
    items = [i for i in items if i.startswith(key)]

    items.sort()
vccccccc
    return items

def function1():
    a = 13
    b = 6
    # print(locals())
    print(function2(**locals()))

def function2(a, b):
    return a

function1()
input1 = {"b": 1, "a": 2}
print(function2(**input1))
# count_unique_word()

testee1 = ["abc", "bcd", "cef", "abc", "ab", "z", "zz"]
print(alphabetical_sorting(testee1, "ab"))