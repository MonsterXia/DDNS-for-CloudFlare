import requests

# Your CloudFlare API Token
API_TOKEN = ""

# Your CloudFlare Zone ID
ZONE_ID = ""

url = f"https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records"
headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

# Send GET Request
response = requests.get(url, headers=headers)

# If Success
print("Status Code:", response.status_code)

class Record:
    def __init__(self, json):
        self.id = json["id"]
        self.zone_id = json["zone_id"]
        self.zone_name = json["zone_name"]
        self.name = json["name"]
        self.type = json["type"]
        self.content = json["content"]
        self.proxiable = json["proxiable"]
        self.proxied = json["proxied"]
        self.ttl = json["ttl"]
        self.settings = json["settings"]
        self.meta=json["meta"]
        self.meta_auto_added=json["meta"]["auto_added"]
        self.meta_managed_by_apps=json["meta"]["managed_by_apps"]
        self.meta_managed_by_argo_tunnel=json["meta"]["managed_by_argo_tunnel"]
        self.comment = json["comment"]
        self.tags = json["tags"]
        self.created_on = json["created_on"]
        self.modified_on = json["modified_on"]

result_obj = response.json()["result"]
for json in result_obj:
    record = Record(json)
    print("--------------------------------")
    print(f"Record ID: {record.id}")
    print(f"Record Name: {record.name}")
    print(f"Record Type: {record.type}")
    print(f"Record Content: {record.content}")

