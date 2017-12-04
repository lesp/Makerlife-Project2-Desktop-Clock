#!/usr/bin/env python3

import time
import feedparser
import scrollphathd
from scrollphathd.fonts import font3x5
from random import randint

scrollphathd.set_brightness(0.2)
scrollphathd.rotate(degrees=180)

def get_time():
    scrollphathd.clear()
    scrollphathd.show()
    current_time = time.ctime()
    current_time = current_time[11:16]
    scrollphathd.write_string(current_time, x=0, y=1, font=font3x5)
    scrollphathd.show()

def get_news():
    scrollphathd.clear()
    scrollphathd.show()
    Pinews = feedparser.parse("https://www.raspberrypi.org/feed/") 
    headline = Pinews["entries"][randint(0,5)]["title"]
    scrollphathd.write_string(headline + "      ", x=0, y=1, font=font3x5)
    status_length = scrollphathd.get_buffer_shape()
    status_length = status_length[0]
    while status_length > 0:
        scrollphathd.show()
        scrollphathd.scroll()
        time.sleep(0.1)
        status_length -= 1

while True:
    get_time()
    time.sleep(5)
    get_news()
