import subprocess
import shlex

command = "docker compose -f compose.yaml up"
process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)

while process.poll() is None:
    output = process.stdout.readline().decode("utf-8").strip()
    if (len(output) > 0):
        print(output)
