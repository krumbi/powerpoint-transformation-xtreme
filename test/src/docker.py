import argparse
from time import sleep

parser = argparse.ArgumentParser(description='Process some integer')
parser.add_argument('integer', metavar='N', type=int,)
parser.add_argument('name', metavar='Name', type=str,)
args = parser.parse_args()


for i in range(0, args.integer):
    print(f"Step done {i} in {args.name}")
    sleep(1)
