import urllib
import urllib.request
import json
import sys

def g_search(phrase,myurl):
    for i in range(0,2):
        rank = "50+"
        r_url = " "
        req_url = "https://www.googleapis.com/customsearch/v1?hl=ja&key=AIzaSyCq-7FGp-Ajs3WNyztnXfxaXyiNGRgPS5A&cx=001377698991619088492:szomgrubcfq&alt=json&q="+ phrase +"&start="+ str(i+1)
        print(req_url)
        headers={'User-Agent': 'Mozilla/5.0'}
        #headers = {"User-Agent": 'Mozilla /5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B5110e Safari/601.1'}
        req = urllib.request.Request(req_url,headers=headers)
        res = urllib.request.urlopen(req)
        dump = json.loads(res.read())
        for j in range(len(dump["items"])):
            print(dump['items'][j]['link'])
            if myurl in dump['items'][j]['link']:
                rank = str((i*10)+j+1)
                print(rank)
                r_url = dump['items'][j]['link']
                break
        else:
            continue
        break

    return rank,r_url


def main(phrase,myurl):
    phrase = urllib.parse.quote(phrase)
    rank,r_url = g_search(phrase,myurl)
    #rank = "a"
    #r_url = "b"
    return rank,r_url
