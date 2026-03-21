import random

import sys

import os

print(random.randint(2, 5))

for i in range(2, 5):
    print(i)

print(sys.path)

print(sys.argv[0])
#print(sys.argv[1])
#print(sys.argv[2])
os.chdir("/home/ubuntu")
os.makedirs("new", exist_ok=True)
print(os.listdir("/home/ubuntu"))

os.walk("/home/ubuntu")
for path, dir, files, in os.walk("/home/ubuntu/python"):
    print(path, dir, files)
