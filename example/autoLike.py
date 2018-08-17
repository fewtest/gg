#coding: utf-8
from LineTimeline import *
import time

client = LineTimeline("EvhxhUOYt9Tq0ooIzQV5.Y2BTmJl2+nKQvipLjEVsLq.toUiGoQ6GR4iEgqRnt1C7Oq9XSJat4+fh6x7O8fXsjg=")

while True:
    feed = client.getFeed()
    for x in feed["result"]["feeds"]:
        if x["post"]["postInfo"]["liked"] == False:
            client.likePost(x["post"]["postInfo"]["postId"])
    time.sleep(60)
