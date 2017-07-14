import unittest
import os
import json
import base64
import requests
from augment00_command import auth
import jwt

CREDS_PATH = os.path.join(os.path.dirname(__file__), "augment00_creds_12518459.json")
FIRE_BASE_HOST = "project00-msme.firebaseio.com"

class ModelsTestCase(unittest.TestCase):

    # def setUp(self):
    #     # First, create an instance of the Testbed class.
    #
    #
    #
    # def tearDown(self):
    #     self.testbed.deactivate()


    def testAuth(self):

        print CREDS_PATH

        with open(CREDS_PATH) as f:
            creds = json.loads(f.read())

        config = auth.get_config(creds, "000000007cc9f7e9")

        print "config: ", config

        if config is not None:

            config_files = config["config"]
            public_key = config["public_key"]

            for config_file in config_files:
                if config_file["path"].endswith("env"):
                    env = config_file["text"]
                    print env

            lines = env.split("\n")

            for line in lines:
                if "FIREBASE_TOKEN" in line:
                    access_token = line[line.find("=")+1:]

            print "****************"
            print "access_token: ", access_token
            print "****************"

        # parts = access_token.split(".")
        # print len(parts)
        # #
        # # for part in parts:
        # #     print base64.b64decode(part)
        #
        # key = "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC2OOdTFt0Ej1OP\nWVZqj61UrcC1I0OHlN82b/NqyAcMHs/y3T466E5U5kSlk7fzXsfGyM3XZr4LOdwj\nVyCMwICa9bwZ2ZvrB0L05EJeP1MTtLjev/5cns98TDJ0PHG7ftOX+bI6Z1BqqNix\nzz6taDih7zXImB1Z3h4pxbYJj3wQm1+K7mpP3MbXo8+0jphOy+i7fCAykvte6BuT\nC4ObXaq9Zn4tdTUGIkwHUEer/D69qq99FimHP6ixO/HgabgNL85QhrRwSrMbAqSH\nWBFylsziavPtaOeZanLePGB+fvyGFL0xNkpL/sZwHV7LI1O+afoD+/o6YOLHIUte\nHeuMPj2JAgMBAAECggEADrkSnl4wCxDGMxmy8kGGmIYWFmycJbBrx+W2uK94Zkx3\nsnXuyRVWUuTCB3t5IZL3DZgm4tsHIDgTZyWV2IQrP+9P5z9zqhiNmo92JKWgLEJD\nV6K9RgrXf9cA5+8ET3O5W+5NrgtamNY99UE7SAkuM43001l7BvT74esla1NVC7BR\nxfWosSmkVej6vuK2fzlUP+Qp6Bt8JdIQ9Hz0wqfMcDOaLTA5VGTrXdryR/1oFepc\nlpBB1VX3LMRJ6kzNJma/GN4NEYbTowgFIRQWy/oN0TjDz+jqzbIqmbWf0MYU6YVp\n8wpF2HDm91T6wNzfWp8EMYPsBVL9AR7O38JHwZtHMwKBgQDnIb0jg5ufR/A4pp/J\nG+HSxfEMjziHlYkHb2etReI+3m5m5NSHHLZ3KHL64ljAZulQfxjBZY5nkakulvMt\nySj1tr2UX/fNda8SEseh+B1w6y5ub6NkwXXArlHh4gy85PMzQpRJS/LguX7Ux/+8\nMpToa1CQB+33MPM8QDGqdd4jCwKBgQDJ1AIVY4uPH7uuM9qtz5yzhi64s8vTz6Vi\ncvKjIVBfcCA9eJVn4o9mzDQx+56K3n0+TDqslcPDJ5vJY/AoJVUBaEOe9cuFOgPV\ncSUvmiXcDZvLKl8nAULI3hA+Vw8EezAVlOyXVngTb/TK0dHu5k9cXKR5tlgnJtUD\nm3hLsl6+OwKBgQDZlel4hWz7hb2flzzVFmqBAdbq++k7uopFdZskg6V5iexk8Qci\nKuWbR3j2th7XAgqivQORDQoCdh3Ovkwvzi/BIUdXZwDhauhlG0jUMb+FjeEoFfC7\n6WPxACoVe7iCGwbYOtVeKyF6bSX5Kk6V3QhRxLUS4mQjUPGqxsP6tPtqAQKBgHCD\nbzHrT6bXQvKHV9ZjkfEG0c8H9I49CO7MM/W7IapCwMZkDa5fQCBHoKVop2a1R87O\nAjuqNfr6fr+TphNLVIs3S9M3JWE9CVwY+mkCHy8AqyRkl60P5+JA4X9PW0DdR94Q\nKqDnhIMZe7cBp23uGLndr5dmjtgsrr2XE0Xnxyd3AoGADpH652nokTdJvIMBmtzV\nCiv1HpIgJnmfbd0n+Hflz/HZYN8lO2rJcyCzDk4VFk7T+jgBJtiNWzX0TJzlkWF/\nwv1oiDfGQKdieb68Q+kQowIpyGO/PO31+Gt7NulFuYpg9l9i4n7H12euArMsVoOj\nl0yAa7+xVMd6xqsEF0mQ2gY=\n-----END PRIVATE KEY-----\n"
        #
        # print jwt.decode(access_token, key=key)
        #
        #
        #
        # firebase_url = auth.firebase_url(FIRE_BASE_HOST, "/channels/12518459-bda0-4401-9779-41d0aac0b780.json", access_token)
        #
        # print firebase_url
        #
        # rsp = requests.get(firebase_url)
        #
        # print rsp.content
        #
        # self.assertEqual(rsp.status_code, 200)
        #
        # print rsp.json()
        # #
        # self.fail()


        print self.sign_in_with_custom_token(access_token)

        self.fail()

    def sign_in_with_custom_token(self, token):

        api_key = "AIzaSyBDu9g23GF8eihQLAIyV2WHEMTCLctfXSY"
        request_ref = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyCustomToken?key={0}".format(api_key)
        headers = {"content-type": "application/json; charset=UTF-8"}
        data = json.dumps({"returnSecureToken": True, "token": token})
        request_object = requests.post(request_ref, headers=headers, data=data)
        return request_object.json()