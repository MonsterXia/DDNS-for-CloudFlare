# DDNS-for-CloudFlare
Synchronize local IP to CloudFlare DNS

## Prepare

Paste API_TOKEN and ZONE_ID in GetRecord.py and MacDDNS.py

Run GetRecord.py to get Record IDs

Copy target Record IDs and paste in MacDDNS.py

## Usage

### EDIT

```sh
crontab -e
```

e.g. every 6 h do 

```sh
0 */6 * * * python Documents/MacDDNS/MacDDNS.py
```

### CHECK

```sh
crontab -l
```

### DELETE

```sh
crontab -r
```

