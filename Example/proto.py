import os
import tempfile
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--key')
parser.add_argument('--value')
args = parser.parse_args()



storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
with open(storage_path, 'w') as f:
    f.write(args.key)
    f.write(args.value)

