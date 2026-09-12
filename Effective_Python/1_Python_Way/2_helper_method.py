from urllib.parse import parse_qs

def get_first_int(query, key, default=0):
    found = query.get(key, [""])
    if found[0]:
        return found[0]
    else:
        return default

if __name__ == "__main__":
    query = "name=Tom&age=0&city="
    query2 = "name=Tom&age=35&job=studnet&job=parttime"

    result = parse_qs(query)
    result2 = parse_qs(query2)

    print(result)
    print(result2)

    name = result.get("name", [""])[0] or 0
    age = result.get("age", [""])[0] or 0
    city = result.get("city", [""])[0] or 0

    print("name : ", name)
    print("age : ", age)
    print("city : ", city)

    age = result.get("age", [""])[0]
    if name:
        name = int(age)
    else:
        name = 0

    print(name)

    name = get_first_int(result, "name")
    age = get_first_int(result, "age")
    city = get_first_int(result, "city")

    print("name : ", name)
    print("age : ", age)
    print("city : ", city)
