from pathlib import Path
import sys

ROOT = Path(__file__).parent

PNG_SIGNATURE = b'\x89PNG\r\n\x1a\n'

png_file_path = ROOT / "algebra_booleana.png"


def is_png(content):
    signature = content[:8]
    return PNG_SIGNATURE == signature

def get_resolution(_content: bytes):
    wide = _content[16: 20]
    hight =  _content[20:24]
    print(wide, hight)

if not png_file_path.is_file():
    print("File not found")
    sys.exit(1)

try:
    with open(png_file_path, "rb") as fin:
        content = fin.read(50)
        if PNG_SIGNATURE == content:
            print("This is a png file.")
            get_resolution(content)
except OSError as err:
    print(err)
    sys.exit(1)