#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status
"""

import requests


if __name__ == "__main__":
    req = requests.get('https://alx-intranet.hbtn.io/status')

    print('Body response:')
    print('\t- type: {_type}'.format(_type=type(req.text)))
    print('\t- content: {_content}'.format(_content=req.text))
