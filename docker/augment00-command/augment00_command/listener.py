
# import requests
# from requests.adapters import ReadTimeout
# import threading
# import json
# import time
# from collections import deque
#
# class SmartDeskListener(object):
#
#     def __init__(self, url):
#
#         self.url = url
#         self.queue = deque()
#         self.thread = None
#         self.alive = threading.Event()
#
#     def start(self):
#         self._StartThread()
#
#     def read(self):
#         try:
#             return self.queue.popleft()
#         except IndexError:
#             return None
#
#     def stop(self):
#         self._StopThread()
#
#     def _StartThread(self):
#         self.thread = threading.Thread(target=self._threadEntry)
#         self.thread.setDaemon(1)
#         self.alive.set()
#         self.thread.start()
#
#     def _StopThread(self):
#         if self.thread is not None:
#             self.alive.clear()          #clear alive event for thread
#             self.thread.join()          #wait until thread has finished
#             self.thread = None
#
#
#     def _threadEntry(self):
#
#         print "starting listener"
#         while self.alive.isSet():
#             buffer = []
#             try:
#                 # print self.url
#                 r = requests.get(self.url, stream=True, timeout=30)
#                 for content in r.iter_content():
#                     # print "content", content
#                     if content == "\n":
#                         if buffer:
#                             as_str = "".join(buffer).decode('string_escape')
#                             print "incomming", as_str
#                             as_str = as_str.strip()
#                             json_str = as_str[1:-1]
#                             try:
#                                 as_dict = json.loads(json_str)
#                                 print as_dict
#                                 self.queue.append(as_dict)
#                             except Exception, e:
#                                 print "json parse failed"
#                                 print e
#                         buffer = []
#                         if not self.alive.isSet():
#                             break
#                     else:
#                         buffer.append(content)
#             except ReadTimeout:
#                 print "timeout"
#             except requests.ConnectionError:
#                 print "timeout"
#
#             time.sleep(1.0)
#             print "starting again"
