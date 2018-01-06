#!/usr/bin/python
from __future__ import print_function
import json
import urllib2
import cookielib

def _get_url_open():
    cookies = cookielib.LWPCookieJar()
    handlers = [
        urllib2.HTTPHandler(),
        urllib2.HTTPSHandler(),
        urllib2.HTTPCookieProcessor(cookies)
        ]
    opener = urllib2.build_opener(*handlers)
    return opener


def _get_url_request(url):
    req = urllib2.Request(url)
    req.add_header('Content-Type', 'application/json')
    return req

def _get_robot_priviledge():
    #get from configuration
    data = {}
    return data

#req = _get_url_request('https://api.github.com/orgs/NAL-i5K/repos')
#opener = _get_url_open()
#response = opener.open(req, json.dumps(_get_robot_priviledge()))

def _read_git_log(repo_name):

    file = "stat.txt"

    result = [repo_name, ]

    cc, fc, ic, dc = (0, 0, 0, 0)
    f = open(file, 'r')
    for line in f:
        line = line.strip()
    if "===" in line:
        num = line.split(" ")[1]
        if num != "0":
            for i in [str(cc), str(fc), str(ic), str(dc)]:
                result.append(i)
        cc, fc, ic, dc = (0, 0, 0, 0)
    else:
        l = line.split(",")
        cc += 1
        for e in l:
            if "changed" in e:
                fc += int(e.split(" ")[0])
            elif "insertion" in e:
                ic += int(e.split("insertion")[0])
            elif "deletion" in e:
                dc += int(e.split("deletion")[0])
    f.close()

    return result

import sys
import os
import subprocess

year = sys.argv[1]

t_result = []
data = json.load(open('repos'))
for d in data:
    if d['fork'] == False: #not forked from other
        repo_name = d['full_name'].split('/')[-1]
        if os.path.exists(repo_name):
            os.chdir(repo_name)
            subprocess.call(["git", "pull", 'origin', 'master'])
            os.chdir('../')
        else:
            subprocess.call(["git", "clone", 'https://github.com/' + d['full_name']])

        os.chdir(repo_name)
        if not os.path.exists('stat.sh'):
            subprocess.call(["ln", '-s', '../stat.sh'])
        subprocess.call("./stat.sh " + year, shell=True)
        result = _read_git_log(repo_name)
        t_result.append(result)
        os.chdir('../')

output_file = open('repo.stat', 'w')
for r in t_result:
    output_file.write(','.join(r) + '\n')
output_file.close()

print('Report generated')
