import json
import os
from pprint import pprint
filename=["citylist.json"]
with open(os.path.join(*filename)) as f:
    data = json.load(f)
print("Loaded")
print(len(data))
print(data[1])
