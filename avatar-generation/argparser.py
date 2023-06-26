import argparse
import pathlib

parser = argparse.ArgumentParser(description='Name')
parser.add_argument('input', metavar='INPUT', type=pathlib.Path, help='the input file')
parser.add_argument('output', metavar='OUTPUT', type=pathlib.Path, help='the output folder')
parser.add_argument("API_KEY", metavar="API_KEY", type=str, help="the API key")
# other arguments

args = parser.parse_args()

# Für input datei:
if not (args.input.is_file() and args.input.suffix == ".txt"):
    parser.error("Input is not a valid txt file")

with open(args.input, "r", encoding='utf-8') as f:
    input_text = f.read()



# Für input ordner:
if not args.input.is_dir():
    parser.error("Input is not a directory")

files = list(args.input.glob("*.txt"))

if len(files) == 0:
    parser.error("Input directory is empty")

for file in files:
    pass
