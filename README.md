# DDNS-for-CloudFlare
Synchronize local IP to CloudFlare DNS

## Prepare

Paste API_TOKEN and ZONE_ID in GetRecord.py and MacDDNS.py

Run GetRecord.py to get Record IDs

Copy target Record IDs and paste in MacDDNS.py

## Usage

Use

```sh
which python
```

to get python dir e.g.

```
/opt/homebrew/anaconda3/bin/python
```

### EDIT

```sh
crontab -e
```

Adding tasks like

```
* * * * * command_to_execute
- - - - -
| | | | |
| | | | +---- day of the week (0 - 7) (Sunday is both 0 and 7)
| | | +------ month (1 - 12)
| | +-------- day of the month (1 - 31)
| +---------- hour (0 - 23)
+------------ minute (0 - 59)
```

e.g. every 6 h do 

```sh
0 */6 * * * cd ~/Documents/MacDDNS && /opt/homebrew/anaconda3/bin/python MacDDNS.py
```

### CHECK

```sh
crontab -l
```

### DELETE

```sh
crontab -r
```

