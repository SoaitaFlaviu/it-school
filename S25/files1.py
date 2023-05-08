from pathlib import Path

R00T = Path(__file__).parent

input_file_path = R00T / "gi.txt"

try:
    with open(input_file_path, 'r') as fin:
       content = fin.read()
except OSError as err:
    print(err)
else:
    for i in content:
        if i.startswith("#"):
         print(i)