import json
import requests
import sys

def get(url):
    response = requests.get(url)
    if not response.ok:
        print(f"Error HTTP status {response.status_code}", file=sys.stderr)
        return
    print(json.dumps(response.json(), indent=4))

def post(url, data):
    response = requests.post(url, json=data)
    if not response.ok:
        print(f"Error HTTP status {response.status_code}", file=sys.stderr)
        return
    print(json.dumps(response.json(), indent=4))

def put(url, data):
    response = requests.put(url, json=data)
    if not response.ok:
        print(f"Error HTTP status {response.status_code}", file=sys.stderr)
        return
    print(json.dumps(response.json(), indent=4))

def delete(url):
    response = requests.delete(url)
    if not response.ok:
        print(f"Error HTTP status {response.status_code}", file=sys.stderr)
        return
    print(json.dumps(response.json(), indent=4))
