import time
import requests


requests.packages.urllib3.disable_warnings()


session = requests.Session()
token = "ACI4ever!"
host = "http://localhost:8000"

data = {
    "ip": "apic-sim-6-0-integration.netcloud.lab",
    "username": "admin",
    "password": "ncpw4Lab.",
}

print("Starting websocket")

while True:
    sleep_time = 120
    try:
        response3 = session.post(
            f"{host}/api/v1/websocket/refresh",
            json=data,
            verify=False,
            timeout=60,
            headers={"Authorization": f"Bearer {token}"},
        )
        print(f"Sleeping for {sleep_time}")
        time.sleep(sleep_time)
    except Exception:
        print("Exception. Starting again")
