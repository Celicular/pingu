import time
import requests
from datetime import datetime

# Hardcoded URL - replace with your target website
URL = "https://example.com"

def ping_website():
    while True:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        try:
            response = requests.get(URL, timeout=10)
            print(f"[{timestamp}] Pinged {URL} - Status: {response.status_code}")
        except requests.RequestException as e:
            print(f"[{timestamp}] Error pinging {URL} - {e}")
        time.sleep(30)

if __name__ == "__main__":
    print(f"Starting website monitoring for {URL}")
    ping_website() 