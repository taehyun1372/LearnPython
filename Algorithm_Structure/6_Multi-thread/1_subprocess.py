import subprocess

result = subprocess.Popen(["cmd", "/c", "echo hello & timeout /t 5 /nobreak & echo goodbye"], creationflags=subprocess.CREATE_NEW_CONSOLE)
print(result)

result = subprocess.Popen(["cmd", "/c", "timeout", "/t", "5", "/nobreak"], creationflags=subprocess.CREATE_NEW_CONSOLE)
print(result)