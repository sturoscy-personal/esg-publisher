import json
import sys

import esgcet.list2json
from esgcet.pub_client import publisherClient
from esgcet.settings import CERT_FN, INDEX_NODE


def main(outdata):

    # 	hostname = args[1]
    # 	cert_fn = args[3]
    hostname = INDEX_NODE
    cert_fn = CERT_FN
    pubCli = publisherClient(cert_fn, hostname)

    d = outdata

    for rec in d:

        new_xml = esgcet.list2json.gen_xml(rec)
        print(new_xml)
        pubCli.publish(new_xml)


#        print(new_xml)
