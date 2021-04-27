import subprocess

res = subprocess.run(["pwd"],stdout = subprocess.PIPE, stderr = subprocess.PIPE)
print(res.stdout.decode("utf8"))