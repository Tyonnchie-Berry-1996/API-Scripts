#!/usr/bin/env python3

import argparse, json, sys
from typing import List, Dict
import requests

UBUNTU_NOTICES_URL = "https://ubuntu.com/security/notices.json"
NVD_CVES_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"

r = requests.get(UBUNTU_NOTICES_URL)
r.raise_for_status()
data = r.json()

for notice in data.get('notices', []):
    release_packages = notice.get('release_packages', {})

    # Skip notices that don't have noble, or handle all releases:
    if 'noble' in release_packages:
        print(f"USN: {notice.get('id')}")
        for pkg in release_packages['noble']:
            print("  -", pkg)
