import os
import tempfile

class File:
    def __init__(self, path):
        self.path = path
        self.path = os.path.abspath(self.path)
        with open(self.path, 'w') as f:
            f.write('')

    def __str__(self):
        return os.path.abspath(self.path)

    def __iter__(self):
        return self

    def __next__(self):
        pass

    def __add__(self, obj):
        pass



    def read(self):
        with open(self.path, 'r') as f:
            return f.read()


    def write(self, data):
        data = str(data)
        with open(self.path, 'w') as f:
            return f.write(data)




f = File('log.txt')
f.write(10)
f.read()