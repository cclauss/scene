# install `scene' module
from __future__ import print_function # Python3 compatible
import shutil
import sys
import os

scene_fn = "scene.so"

def contains(folder, file):
    return file in os.listdir(os.path.join("build", folder))

def run(cmd):
    if (os.system(cmd) != 0):
        sys.exit(1) # Stop if something fails

print("Building")
run("python setup.py build")   # build `scene'
folders = os.listdir("build") # get folders
for folder in folders:
    if contains(folder, scene_fn):
        break
else:
    sys.stderr.write("failed to locate `%s'", scene_fn)
    exit(1)

if not os.path.exists("scene"):
    os.mkdir("scene")

for file in ["scene.py", "_scene_types.py", "sound.py"]:
    print("Moving `%s'" % file)
    shutil.move(file, "scene")

print("Moving `%s'" % scene_fn)
shutil.move(os.path.join("build", folder, scene_fn),
            os.path.join("scene", "_scene.so"))

print("Done.")
