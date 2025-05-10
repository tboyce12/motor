import json
import requests
import sys

def get(url, token=None):
    if token:
        response = requests.get(
            url,
            headers={"Authorization": f"Bearer {token}"}
        )
    else:
        response = requests.get(url)
    if not response.ok:
        print(f"Error HTTP status {response.status_code}", file=sys.stderr)
        return
    print(json.dumps(response.json(), indent=4))

def post(url, data, token=None):
    if token:
        response = requests.post(
            url, json=data,
            headers={"Authorization": f"Bearer {token}"}
        )
    else:
        response = requests.post(url, json=data)
    if not response.ok:
        print(f"Error HTTP status {response.status_code}", file=sys.stderr)
        return
    print(json.dumps(response.json(), indent=4))

def put(url, data, token=None):
    if token:
        response = requests.put(
            url, json=data,
            headers={"Authorization": f"Bearer {token}"}
        )
    else:
        response = requests.put(url, json=data)
    if not response.ok:
        print(f"Error HTTP status {response.status_code}", file=sys.stderr)
        return
    print(json.dumps(response.json(), indent=4))

def delete(url, token=None):
    if token:
        response = requests.delete(
            url,
            headers={"Authorization": f"Bearer {token}"}
        )
    else:
        response = requests.delete(url)
    if not response.ok:
        print(f"Error HTTP status {response.status_code}", file=sys.stderr)
        return
    print(json.dumps(response.json(), indent=4))
