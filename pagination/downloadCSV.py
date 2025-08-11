#!/usr/bin/env python3
"""
Connect api to download csv file
"""
import requests

url = "https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/misc/2020/5/7d3576d97e7560ae85135cc214ffe2b3412c51d7.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20250811%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20250811T060204Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=7cc26edf138d7e4a25f34115b0e232ec8042a1d5b78f4d64f4a676ed7b29aa74"

response = requests.get(url)

if response.ok:
    with open("Popular_Baby_Names.csv", "wb") as f:
        f.write(response.content)
    print("It's works !")
else:
    print("status code: {}".format(response.status_code))
