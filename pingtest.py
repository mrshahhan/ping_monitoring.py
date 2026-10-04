import subprocess
import re
import time

host = "8.8.8.8"

while True:
    result = subprocess.run(
        ["ping", "-n", "1", host],
        capture_output=True,
        text=True,
        encoding="cp866"
    )

    if result.returncode == 0:
        match = re.search(r'(?:time|время)[=<](\d+)\s*m?s?', result.stdout)

        if match:
            ping = match.group(1)
            print(f"Ping: {ping} ms")
        else:
            print("Ответ получен, но ping не найден")

    time.sleep(1)