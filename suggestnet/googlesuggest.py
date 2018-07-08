import argparse
from time import sleep
from string import ascii_lowercase
from string import digits
import urllib
import urllib.request, urllib.error
from urllib.request import Request, urlopen
from urllib.error import URLError
import xml.etree.ElementTree as ET


class GoogleAutoComplete:
    def __init__(self, test_mode=False, recurse_mode=False):
        self.base_url = 'https://www.google.co.jp/complete/search?'\
                        'hl=ja&output=toolbar&ie=utf-8&oe=utf-8&'\
                        'client=firefox&q='
        self.test_mode = test_mode
        self.recurse_mode = recurse_mode
        self.chrs = ['あ', 'g', '1']
        """if test_mode:
            self.chrs = ['あ', 'g', '1']
        else:
            self.chrs = [chr(i) for i in range(ord('ぁ'), ord('う'))]
            self.chrs.extend(ascii_lowercase)
            self.chrs.extend(digits)"""

    def get_suggest(self, query):
        query = urllib.parse.quote_plus(query)
        url = 'https://www.google.com/complete/search?hl=en&output=toolbar&q='+ query
        req = urllib.request.Request(url)
        xml_dict = {}
        suggest_list = []

        with urllib.request.urlopen(req) as response:
            XmlData = response.read()
            root = ET.fromstring(XmlData)

        for suggestion in root.iter('suggestion'):
            xml_dict = suggestion.attrib
            a = str(xml_dict.values())
            a = a[14:]
            a = a[:-3]
            suggest_list.append(a)
        print(suggest_list)
        sleep(1)
        return suggest_list

    def get_suggest_with_one_char(self, query):
        # キーワードそのものの場合のサジェストワード
        ret = self.get_suggest(query)

        # キーワード＋空白の場合のサジェストワード
        ret.extend(self.get_suggest(query + ' '))

        # キーワード＋空白＋1文字の場合のサジェストワード
        for ch in self.chrs:
            ret.extend(self.get_suggest(query + ' ' + ch))

        # -rオプションがあればもう1段階
        if self.recurse_mode:
            ret = self.get_uniq(ret)  # 事前に重複を除いておく
            newone = []
            for ph in ret:
                ph_list = self.get_suggest(ph + ' ')
                try:
                    ph_list.remove(ph)
                except:
                    pass
                ph_list.insert(0,ph)
                newone += [ph_list]
            #ret.extend(addonelevel)

        return newone

    # 重複を除く
    def get_uniq(self, arr):
        uniq_ret = []
        for x in arr:
            if x not in uniq_ret:
                uniq_ret.append(x)
        return uniq_ret

def g_suggest(phrase):

    # Google Suggest キーワード取得
    gs = GoogleAutoComplete(recurse_mode = "--recure")
    newone = gs.get_suggest_with_one_char(phrase)
    return newone
    """ファイルに保存する
    fname = filename
    with open(fname, 'w') as fs:
        for key in ret:
            fs.write(key + "\n")"""
