# -*- coding: utf-8 -*-

import requests
import json
import os
import wget
import cv2
#import numpy as np
import sys
import re

"""

[ディレクトリ構成]
- master/(path) : マスターとなるディレクトリのパスを指定
| - setting.d   : 設定ファイル(何番目の画像ファイルからダウンロードするかを表すイテレータ)
| - download/   : 画像保存先

[注意]
setting.dは1から101-NUMの間の値に設定しないとエラーが返されるので、注意してください。

[変数]
NUM             : ダウンロードする画像の数
searchTerm      : 検索ワード

"""
key = '**自分のAPI KEY**'
cx = '**自分のCSE ID**'

#absolute path
path = '**絶対パス**'

#output path for images
output_path = path + 'download/'

#Setting files
setting = path + 'setting.d'

#Search Keyword
searchTerm = u'検索ワード(日本語も可能)'

#Num of Results(images)
### [MUST] if integer of setting.d is not between 1 and (101-num), modify it.
NUM = 10


def img_dl() :
    f = open(setting,'r+w')
    for line in f:
        startIndex = int(line)
    value_write = startIndex + NUM
    f.seek(0)
    f.write(str(value_write))
    f.close()

    searchUrl = "https://www.googleapis.com/customsearch/v1?q=" + \
searchTerm + "&start=" + str(startIndex) + "&key=" + key + "&cx=" + cx + \
    "&num=" + str(NUM) + "&searchType=image"
    list = []

    os.chdir(output_path)

    #searchTerm to image urls
    r = requests.get(searchUrl)
    response = r.content.decode('utf-8')
    result = json.loads(response)

    #for check
    #print response
    #print result

    #image urls to list
    for i in range(0,NUM) :
        tmp  = result["items"][i]["link"]
        print "Downloading...:" + tmp
        list.append(tmp)

    #download images via wget
    for url in list:
        print url
        wget.download(url)
 

def run() :    
    img_dl()

if __name__ == '__main__':
    run()
