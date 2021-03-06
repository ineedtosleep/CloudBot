"""
Format all JSON files in the bot core in a consistent manor
"""

from pathlib import Path
import collections
import codecs
import json

path = Path().resolve()

for file in path.rglob("*.json"):
    print(file)
    with file.open(encoding='utf8') as f:
        data = json.load(f, object_pairs_hook=collections.OrderedDict)

    with file.open('w', encoding='utf8') as f:
        print(json.dumps(data, indent=4), file=f)

