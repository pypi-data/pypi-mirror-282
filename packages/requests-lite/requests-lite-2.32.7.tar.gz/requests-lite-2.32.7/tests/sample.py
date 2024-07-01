import time
import requests_lite as requests
r = requests.get("https://httpbin.org/anything")

print(r.text)

time.sleep(10)

print("Closing program")
requests.utils.free_resources()