import re

pattern1 = r"[a-c]" # between a and c
print(re.fullmatch(pattern1, "a"))
print(re.fullmatch(pattern1, "b"))
print(re.fullmatch(pattern1, "c"))
print(re.fullmatch(pattern1, "d"))

pattern2 = r"[^5]" # anthing not 5 
print(re.fullmatch(pattern2, "4"))
print(re.fullmatch(pattern2, "a"))
print(re.fullmatch(pattern2, "5"))

pattern3 = r"[\d]" # only digit
print(re.fullmatch(pattern3, "4"))
print(re.fullmatch(pattern3, "10"))

pattern4 = r"[\D]" # anything not digit 
print(re.fullmatch(pattern4, "4"))
print(re.fullmatch(pattern4, "10"))
print(re.fullmatch(pattern4, "a"))

pattern5 = r"[\s]" # only space 
print(re.fullmatch(pattern5, " "))

pattern6 = r"[\S]" # anything not space 
print(re.fullmatch(pattern6, "9"))
print(re.fullmatch(pattern6, "A"))
print(re.fullmatch(pattern6, " "))

pattern7 = r"[\w]" # anything alphabet or digit 

print(re.fullmatch(pattern7, "9"))
print(re.fullmatch(pattern7, "w"))
print(re.fullmatch(pattern7, " "))


pattern8 = r"[\W]" # anything alphabet or digit 

print(re.fullmatch(pattern8, "9"))
print(re.fullmatch(pattern8, "w"))
print(re.fullmatch(pattern8, " "))

pattern9 = r"[abc]" # between a and b and c
print(re.fullmatch(pattern9, "a"))
print(re.fullmatch(pattern9, "c"))
print(re.fullmatch(pattern9, "d"))

pattern10 = r"[0-9][0-8][0-7][0-6]" # 0000~9876 000 does not match
print(re.fullmatch(pattern10, "000"))
print(re.fullmatch(pattern10, "0000"))
print(re.fullmatch(pattern10, "0007"))

pattern11 = r"[a-z0-8]" # range between a to z and between 0 to 8
print(re.fullmatch(pattern11, "a"))
print(re.fullmatch(pattern11, "Z"))
print(re.fullmatch(pattern11, "8"))
print(re.fullmatch(pattern11, "9"))

pattern12 = r"ca*t"
print(re.fullmatch(pattern12, "ct"))
print(re.fullmatch(pattern12, "cat"))
print(re.fullmatch(pattern12, "caat"))
print(re.fullmatch(pattern12, "caabt"))

pattern13 = r"ca+t"
print(re.fullmatch(pattern13, "ct"))
print(re.fullmatch(pattern13, "cat"))
print(re.fullmatch(pattern13, "caat"))
print(re.fullmatch(pattern13, "caabt"))

pattern14 = r"ab{1,3}c"
print(re.fullmatch(pattern14, "ac"))
print(re.fullmatch(pattern14, "abc"))
print(re.fullmatch(pattern14, "abbc"))
print(re.fullmatch(pattern14, "abbbc"))
print(re.fullmatch(pattern14, "abbbbc"))

pattern15 = r"[\d]{6}-{1}[\d]{7}"
print(re.fullmatch(pattern15, "000000-0000000"))
print(re.fullmatch(pattern15, "000000--0000000"))
print(re.fullmatch(pattern15, "00000-0000000"))

pattern16 = r"(28|29|30)"
print(re.fullmatch(pattern16, "128"))
print(re.search(pattern16, "128"))

pattern17 = r"^(28|29|30)"
print(re.fullmatch(pattern17, "128"))
print(re.search(pattern17, "128"))

pattern18 = r"[1-9][0-9]{3}"
pattern19 = r"[a-zA-Z]{5}"
pattern20 = r"[A-Z]{3}-[\d]{4}"