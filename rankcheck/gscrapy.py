from collections import namedtuple
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = Options()

# ヘッドレスモードを有効にする
options.add_argument('--headless')


# 検索結果を1件ずつ格納する名前付きタプル
SearchResultRow = namedtuple(
    'SearchResultRow',
    ['title', 'url', 'display_url', 'dis']
)


def get_text_or_none(element, num):
    """
    <div class='spam'>
      <a>リンク1-1</a>
      <a>リンク1-2</a>
      <a>リンク1-3</a>
    </div>
    <div class='spam'>
      <a>リンク2-1</a>
    </div>
    のようなHTMLから、テキストを取得する際に使います

    for row in driver.find_elements_by_css_selector('div.spam'):
        a_element = row.find_elements_by_tag_name('a')
        a1 = get_elements_of_one(a_element, 0)
        a2 = get_elements_of_one(a_element, 1)
        a3 = get_elements_of_one(a_element, 2)
    """

    try:
        return element[num].text
    except IndexError:
        return ''


class GoogleScrapy:

    def __init__(self, keyword, end=1, default_wait=3):
        self.url = 'https://www.google.co.jp?pws=0'
        self.keyword = keyword
        self.end = end
        self.default_wait = default_wait
        self.driver = None
        self.searches = [[] for x in range(end)]
        self.ads = [[] for x in range(end)]
        self.relations = [[] for x in range(end)]

    def enter_keyword(self):
        """キーワードを入力し、エンターを押す"""

        self.driver.get(self.url)
        self.driver.find_element_by_id('lst-ib').send_keys(self.keyword)
        self.driver.find_element_by_id('lst-ib').send_keys(Keys.RETURN)

    def next_page(self):
        """次のページへ移動する"""

        self.driver.find_element_by_css_selector('a#pnnext').click()
        time.sleep(self.default_wait)

    def get_search(self, page):
        """通常の検索結果を取得する"""

        all_search = self.driver.find_elements_by_class_name('rc')
        for data in all_search:
            title = data.find_element_by_tag_name('h3').text
            url = data.find_element_by_css_selector(
                'h3 > a').get_attribute('href')
            display_url = data.find_element_by_tag_name('cite').text
            try:
                dis = data.find_element_by_class_name('st').text
            except NoSuchElementException:
                dis = ''

            result = SearchResultRow(title, url, display_url, dis)
            self.searches[page].append(result)

    def start(self):
        """　ブラウザを立ち上げ、各種データの取得を開始する"""
        try:
            self.driver = webdriver.Chrome(chrome_options=options,executable_path='rankcheck/chromedriver')
            self.driver.implicitly_wait(self.default_wait)
            self.enter_keyword()
            for page in range(self.end):
                self.get_search(page)
                self.next_page()
        finally:
            self.driver.quit()
