import json
import sys
from .gscrapy import GoogleScrapy


def g_search_s(phrase,myurl):
    google = GoogleScrapy(phrase, end=5, default_wait=3)
    google.start()
    for page_num, rows in enumerate(google.searches, 1):
        for rankinpage,row in enumerate(rows):
            r_url = row.url
            print(r_url)
            if myurl in r_url:
                rank = str(((page_num-1)*10)+rankinpage+1)
                break
            else:
                rank = "50+"
                r_url = "圏外です"
        else:
            continue
        break

    return rank,r_url


def main(title_list,myurl):
    rank_list , url_list = [] , []
    for phrase in title_list:
        print(phrase)
        rank,r_url = g_search_s(phrase,myurl)
        rank_list.append(rank)
        url_list.append(r_url)
    #rank = "a"
    #r_url = "b"
    return rank_list , url_list

# phrase = "統計学"
# myurl = "https://to-kei.net/"
# rank,r_url = g_search_s(phrase,myurl)
