import os
import tempfile
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("--key")
parser.add_argument("--value")
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
args = parser.parse_args()
key = args.key
value = args.value
open(storage_path, 'a').close()
with open(storage_path, 'r+') as f:
    if key and value:

        if os.stat(storage_path).st_size == 0:
            storage = {}
        else:
            storage = json.loads(f.read())
            f.seek(0)

        if storage.get(key) is None:
            storage[key] = [value]
        else:
            storage[key].append(value)

        json.dump(storage, f)
    elif key:

        string = ""
        if os.stat(storage_path).st_size != 0:
            storage = json.load(f)
            if key in storage:
                for i in storage[key]:
                    string += i + ', '
        print(string[:-2])