from pathlib import Path
from datetime import datetime
working_dir = Path('.') # current working directory

print(working_dir)
print(f"Current working directory: {working_dir.absolute()}")
script_path = Path(__file__)
print(f"Script path: {script_path}")
print(f"Script parent directory {script_path.parent}")

print(f"{script_path} exists? {script_path.exists()}")

start_time_path = script_path.parent / "program_data" / "start_time.txt"

#if not start_time_path.parent.exists():
    #start_time_path.parent.mkdir()
    #mkdir = make directory
    #print(f"Created {start_time_path.parent}")


# w = scriere text
# r = citire text 
# a = adaugare text 
# wb = scriere binara
# rb = citire binara
# ab = adaugare binara

start_time_path.mkdir(exist_ok=True, parents=True)

print(start_time_path.is_dir())
print(start_time_path.is_file())

now = datetime.now()
now_file_name = now.strftime("%Y%m%d_%H%M%S")


with open(start_time_path / now_file_name, "w") as fout: # fout = file descriptor(orice)
    fout.write("No errors")
    pass

print("File operation done!")

#script care citeste numele nostru si creem un fisier care e in acelasi folder cu scriptul

