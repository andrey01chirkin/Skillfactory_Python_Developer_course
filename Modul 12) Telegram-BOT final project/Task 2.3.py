import json
from pprint import pprint

import requests

r = requests.get("https://baconipsum.com/api/?type=all-meat&paras=3&start-with-lorem=1")
texts = json.loads(r.content)

pprint(texts[0])

