import websocket
import time
import thread

FIREBASE_HOST = "console.firebase.google.com/project/project00-msme/database/data"
UUID = "1020e9bd-cab6-4182-8b17-31d1b5851876"
TOKEN = "eyJhbGciOiAiUlMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ1aWQiOiAiMTAyMGU5YmQtY2FiNi00MTgyLThiMTctMzFkMWI1ODUxODc2IiwgImlzcyI6ICJ0ZXN0QGxvY2FsaG9zdCIsICJleHAiOiAxNDk3NDcwNzk4LCAiaWF0IjogMTQ5NzM4NDM5OCwgImF1ZCI6ICJodHRwczovL2lkZW50aXR5dG9vbGtpdC5nb29nbGVhcGlzLmNvbS9nb29nbGUuaWRlbnRpdHkuaWRlbnRpdHl0b29sa2l0LnYxLklkZW50aXR5VG9vbGtpdCIsICJzdWIiOiAidGVzdEBsb2NhbGhvc3QifQ==.d+C6HhzRW91zdvJ2Ey9eUmaQwqv24yziQwEDMnAYmOLMg12z+VgMUc7HYVMHJKdnV3X9oCXcW+T+7+hrhn2SG6jAUsYX9d0yTrDuF7EOfDQe4EApAby6H5eb8tzQHR+WwZPVAdPkYWl20zSNsvAaDMmWeqVbgBEbFhipwtka6bOqWzPzg+Ca1wiP9TBD9QsL/gNHMr4Tp/mGmUMDEgo5KghVd7guQJnuW5hwWqGbu3syR79kVER+ZOHxdcFRFt3ck92fPsADYzlm8JJwZIefZzOt+F6mmpGCAIMBlYWlng1BWcSFCUCR5nPhsbrSg+qd0HhWJ3xb8PzT2lidqHd5Og=="


def on_message(ws, message):
    print "*************  fuck"
    print message

def on_error(ws, error):
    print error

def on_close(ws):
    print "### closed ###"

def on_open(ws):
    print "********  oprning  ***********"
    def run(*args):
        for i in range(3):
            time.sleep(1)
        time.sleep(1)
        ws.close()
        print "thread terminating..."
    thread.start_new_thread(run, ())


if __name__ == "__main__":

    url = "wss://%s/channels/%s.json?auth=%s" % (FIREBASE_HOST, UUID, TOKEN)

    print url

    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(url,
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()