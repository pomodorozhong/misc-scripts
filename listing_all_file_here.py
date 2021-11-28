import glob
import os
import json
import sys


abs_path = os.path.abspath(os.getcwd())
dest_dir = os.path.join(abs_path, "*")
ordered = sorted(glob.glob(dest_dir))

file_out = sys.argv[1]
out = json.dumps(ordered)
with open(file_out, "w") as fp:
    print(out, file=fp)
