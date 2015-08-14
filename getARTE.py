#!/usr/bin/python
# utf-8
import sys
import requests

#we retrieve the argument which is the arte url
#default output of the flv file
output = "a.out"
videoUrl = "http://www.arte.tv/guide/fr/direct"

r = requests.get(videoUrl)

r.encoding = "utf-8"
import re
m = re.search('http.*livestream.*\'\s', r.content)
livestream = m.group(0).rstrip().rstrip("'")

print livestream
r_json = requests.get(livestream)
data = r_json.json()

# print data['videoJsonPlayer']
rtmpurl = data['videoJsonPlayer']['VSR']['RMTP_HQ']['streamer'] + data['videoJsonPlayer']['VSR']['RMTP_HQ']['url']
import subprocess
# rtmpdump -v -r "rtmp://artestras.fc.llnwd.net/artestras/s_artestras_scst_geoFRDE_fr?s=1320220800&h=d0ae27535aafda72395535f3b657c607" -o test.flv
stdout = open("stdout.txt","wb")
stderr = open("stderr.txt","wb")
#mp=subprocess.call(['/usr/bin/rtmpdump', '-v', '-r', rtmpurl, '-o', '/tmp/test.flv'], stdout=stdout, stderr=stderr)
#mpPID=mp.pid
#print mpPID
p=subprocess.Popen('/usr/bin/rtmpdump -v -r "' + rtmpurl + '" -o /tmp/test.flv', stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
# for line in p.stdout.readlines():
#     print line,

retval = p.wait()
