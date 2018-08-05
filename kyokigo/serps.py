import urllib
import urllib.request
import json
import sys

def scrape_serps(phrase,maxrank):
    url_list = []
    for i in range(0,maxrank):
        req_url = "https://www.googleapis.com/customsearch/v1?hl=ja&key=AIzaSyCq-7FGp-Ajs3WNyztnXfxaXyiNGRgPS5A&cx=001377698991619088492:szomgrubcfq&alt=json&q="+ phrase +"&start="+ str(i+1)
        headers={'User-Agent': 'Mozilla/5.0'}
        #headers = {"User-Agent": 'Mozilla /5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B5110e Safari/601.1'}
        req = urllib.request.Request(req_url,headers=headers)
        res = urllib.request.urlopen(req)
        dump = json.loads(res.read())
        for j in range(len(dump["items"])):
            #print(dump['items'][j]['link'])
            url_list.append(dump['items'][j]['link'])
        return url_list

def g_serps(key,maxrank):
    urls = []
    key = urllib.parse.quote(key)
    url_list = scrape_serps(key,maxrank)
    return url_list
