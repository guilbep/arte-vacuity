#!/usr/bin/python

import sys,urllib,re

#we retrieve the argument which is the arte url
#default output of the flv file
output = "a.out"
videoUrl = ""

try:
    videoUrl = sys.argv[1]
    if sys.argv == 3:
      output = sys.argv[2]
    # retrieve the page at the url
    page = urllib.urlopen(videoUrl)
    # "videorefFileUrl=" 
    
    try:
      line = page.readlines()
      #print line
      re.search("videorefFileUrl",page.readline())
      #print re.group(0)
    except:
      print "regexp failed"
    # <object type=\"application/x-shockwave-flash\" id=\"playerVideo\" data=\"
    #print page.read()
    # parse it to find sfw player url
    # parse it to find rtmp file url
except:
  print "not enough arguments"
