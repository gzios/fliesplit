import sys
import linecache
import math
import os

flie_type = 0
if(len(sys.argv) > 4):
    flie_type = int(sys.argv[4])
strs = linecache.getlines(sys.argv[1])
strs = [x for x in strs if len(x.strip()) > 0]
file_name = os.path.basename(sys.argv[1])
out_path = sys.argv[2]
lines = len(strs)
split = int(sys.argv[3])
linesp = int(math.ceil(lines/float(split)))
if(flie_type == 1):
    linesp = split
for i in range(0, lines, linesp):
    break_file_name = os.path.splitext(file_name)
    new_file_name = "{}_{}{}".format(
        break_file_name[0], int(i/linesp), break_file_name[1])
    textstr = strs[i:i+linesp]
    with open(os.path.join(out_path, new_file_name), 'w') as f:
        f.writelines(textstr)
