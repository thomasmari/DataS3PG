import os
import glob
import random

print(glob.glob("/files_names/*"))
for f in glob.glob("/files_names/*"):
    os.rename(f,f[:-1]+random.randint(3, 9))
print(glob.glob("/files_names/*"))
