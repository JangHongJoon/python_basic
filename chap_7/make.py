import os

for path in os.listdir():
    if os.path.isdir(path):
        print(path) 