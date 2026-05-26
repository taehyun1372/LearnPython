fn = "AAPL_history.csv"
with open(fn, 'r') as f:
    for _ in range(100):
        print(f.readline(), end='')
