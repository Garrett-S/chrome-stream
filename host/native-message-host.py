#!/usr/local/bin/python

import struct
import sys
import Queue
import os
import json

def 

def Main():
    quality = "source"
    streamURL = "http://www.twitch.tv/wagamamatv"

    pid = os.fork()
    if pid == 0:
        args = ["livestreamer", streamURL, quality]
        os.execvp("livestreamer", args)



if __name__ == '__main__':
      Main()
