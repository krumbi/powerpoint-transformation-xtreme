import argparse
from time import sleep

parser = argparse.ArgumentParser(description='Process some integer')
parser.add_argument('integer', metavar='N', type=int,)
args = parser.parse_args()


for i in range(0, args.integer):
    print(f"Step done {i}")
    sleep(1)
