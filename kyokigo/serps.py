import json
import sys
from .gscrapy import GoogleScrapy


def g_search_s(phrase, maxrank):
    urls = []
    google = GoogleScrapy(phrase, end=maxrank, default_wait=3)
    google.start()
    for page_num, rows in enumerate(google.searches, 1):
        for rankinpage, row in enumerate(rows):
            print(row.url)
            urls.append(row.url)

    return urls
