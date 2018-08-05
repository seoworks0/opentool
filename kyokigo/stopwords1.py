import urllib.request, urllib.error
import sys
from collections import Counter
from bs4 import BeautifulSoup

#html = urllib.request.urlopen("http://svn.sourceforge.jp/svnroot/slothlib/CSharp/Version1/SlothLib/NLP/Filter/StopWord/word/Japanese.txt")
#soup = BeautifulSoup(html, "html.parser")

def stopwords(l1):
    f = open('kyokigo/Japanese.txt')
    areas = f.read().split()
    f.close()
    l2 = set(areas)
    list_ab =  list(filter(lambda x: x not in l2, l1))
    return list_ab
