import time
import os

if __name__ == '__main__':

    augment00_uuid = os.environ.get("AUGMENT00_UUID")

    while True:
        print "hello from augment00 %s" % augment00_uuid
        time.sleep(60)