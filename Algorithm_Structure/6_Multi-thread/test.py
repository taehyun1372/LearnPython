message = "task1\ntask2\ntask3\n"
buffer = message
line, buffer = buffer.split("\n", 1)
print(line, buffer)
line, buffer = buffer.split("\n", 1)
print(line, buffer)
line, buffer = buffer.split("\n", 1)
print(line, buffer)