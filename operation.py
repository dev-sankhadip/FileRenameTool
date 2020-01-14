import os

class Operation:

    def read(path):
        files = os.scandir(path)
        for f in files:
            print(f)