import urllib.request
import json

with urllib.request.urlopen("https://ipinfo.io/json") as url:
    data = json.loads(url.read().decode())
    print(data)
