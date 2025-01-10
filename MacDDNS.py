import os
import json
import requests
from urllib3.exceptions import MaxRetryError, SSLError
# Ignore proxy
os.environ['no_proxy'] = '*'

# CloudFlare API URL
CLOUDFLARE_API_URL = "https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records/{record_id}"

# Your CloudFlare API Token
API_TOKEN = ""

# Your CloudFlare Zone ID
ZONE_ID = ""

# Your DNS Record ID
RECORD_ID_v4 = ""
RECORD_ID_v6 = ""

def get_current_ip_v4():
    response = requests.get('http://httpbin.org/ip')
    if response.status_code == 200:
        ip_data = response.json()
        current_ip = ip_data['origin']
        return current_ip
    else:
        raise Exception('Failed to get current IP')

def get_current_ip_v6():
    response = requests.get('https://ipv6.icanhazip.com')
    if response.status_code == 200:
        ipv6_address = response.text.strip()
        return ipv6_address
    else:
        raise Exception('Failed to get IPv6 address')

def update_cloudflare_dns(ip, mode):
    if mode == "4":
        Record_id = RECORD_ID_v4
        type = "A"
    elif mode == "6":
        Record_id = RECORD_ID_v6
        type = "AAAA"
    else:
        raise Exception('Invalid mode')

    url = CLOUDFLARE_API_URL.format(zone_id=ZONE_ID, record_id=Record_id)
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "type": f"{type}",  # Adjust accordingly if you need different record type
        "name": "mac.246801357.xyz",  # e.g., "example.com" or "sub.example.com"
        "content": ip,
        "ttl": 1,  # Automatic TTL
        "proxied": True  # Set to True if you want CloudFlare to proxy the request
    }

    response = requests.put(url, data=json.dumps(payload), headers=headers)
    if response.status_code == 200:
        print(f'IPv{mode} update successful')
    else:
        print(f'IPv{mode} update failed')
        print(response.json())

def sync_ip_to_cloudflare():
    try:
        current_ip_v4 = get_current_ip_v4()
        current_ip_v6 = get_current_ip_v6()
        update_cloudflare_dns(current_ip_v4, "4")
        update_cloudflare_dns(current_ip_v6, "6")
        print(f"IPv4 address: {current_ip_v4}")
        print(f"IPv6 address: {current_ip_v6}")
    except SSLError as e:
        print(f"SSL error occurred: {e}")
    except MaxRetryError as e:
        print(f"Max retries exceeded: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return None

if __name__ == "__main__":
    sync_ip_to_cloudflare()