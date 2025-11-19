import os
from BZ_API import api
import urllib3
import bugzilla
import re
from time import sleep
import json
import requests


urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs="/etc/ssl/certs/ca-bundle.trust.crt")

def product_finder():

    try:
        URL = "bugzilla.redhat.com/"

        r = requests.get(f"http://{URL}/rest/product_selectable")

        data_set = r.json()

        json_id = json.dumps(data_set, indent=2)

        with open('id_advisories.json', 'w') as e:
            e.write(json_id)

        with open("id_advisories.json", 'r') as e:
            id_object = json.loads(e.read())

        
        for x in range(0, id_object):
            product_id = id_object['ids'][x]

            r = requests.get(f"http://{URL}rest/product/{product_id}")

            new_set = r.json()

            json_id = json.dumps(new_set, indent=2)

            print(json_id)

    except IndexError:
        pass


def bugz_finder():

    api_key = api

    URL = "bugzilla.redhat.com/"

    bzapi = bugzilla.Bugzilla(URL, api_key=api_key, force_rest=True)
    assert bzapi.logged_in
    
    query = bzapi.build_query(product="Fedora",
                              component="kernel",
                              status="NEW"
                              )

    bugs = bzapi.query(query)

    for i in range(0, len(bugs)):
        matches = re.findall(r"[#]\d{1,10}", str(bugs[i]))
        sleep(2)

        bug_num = matches[0]
        bug_id = bug_num[1:len(bug_num) - 1 + 1]

        with open('bz-data.txt', 'a') as e:
            e.write(str(bug_id) + "\n")

        hoping = bzapi.build_query(dependson=bug_id)

        dependson = bzapi.query(hoping)

        print("\n" + f"Found {len(dependson)} bugs with in query")

        for i in range(0, 1):

            matched = re.findall(r"[#]\d{1,10}", str(dependson[i]))
            print("\nRetrieving public tracking BZ")
            sleep(3)

            bug_numz= matched[0]
            id_bug = bug_numz[1:len(bug_numz) - 1 + 1]
            link = "https://bugzilla.redhat.com/show_bug.cgi?id=" + id_bug
            
            print(dependson[i],"\n",link)

            sleep(3)

if __name__ == '__main__':
    # product_finder()
    bugz_finder()


