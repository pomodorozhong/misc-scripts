import glob
import os
import json
import sys

try:
    arg_command = sys.argv[1]
except IndexError:
    print("you are missing the path of output file.")
    exit()

abs_path = os.path.abspath(os.getcwd())
dest_dir = os.path.join(abs_path, "*")
ordered = sorted(glob.glob(dest_dir))

file_out = arg_command
out = json.dumps(ordered)
with open(file_out, "w") as fp:
    print(out, file=fp)
