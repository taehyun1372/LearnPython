import pandas as pd

test_reslt = []
data1 = {
    "device": "AT1091750441BM",
    "UAT" : "UAT_2026-09-08-15-55-48",
    "testdate" : "2026-09-08 15:55:4",
    "lastpass" : 10,
    "firstfail" : 0,
    "passcount" : 15,
    "failcount" : 0,
    "skipcount" : 0,
    "passed" : True
}

data2 = {
    "device": "AT1091750440BM",
    "UAT" : "UAT_2026-09-08-15-55-48",
    "testdate" : "2026-09-08 15:55:4",
    "lastpass" : 7,
    "firstfail" : 8,
    "passcount" : 10,
    "failcount" : 1,
    "skipcount" : 5,
    "passed" : True
}

test_reslt.append(data1)
test_reslt.append(data2)

df = pd.DataFrame(test_reslt)
print(df.head())