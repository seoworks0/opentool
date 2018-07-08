from .googlesuggest import g_suggest
import json
import re
#import requests
import collections as cl

def main(phrase):
    vol = 1000
    ret = g_suggest (phrase)
    #ret = [['データサイエンティスト 資格', 'データサイエンティスト 資格 難易度', 'データサイエンティスト 資格 emc', 'データサイエンティスト 資格 費用', 'データサイエンティスト 資格 価格', 'データサイエンティスト 転職 資格'], ['データサイエンティスト 転職', 'データサイエンティスト 転職 エージェント', 'データサイエンティスト 転職 資格'], ['データサイエンティスト 勉強'], ['データサイエンティスト とは'], ['データサイエンティスト アナリスト', 'データサイエンティスト アナリスト 違い'], ['データサイエンティスト アメリカ', 'データサイエンティスト 大学院 アメリカ', 'アメリカ データサイエンティスト 年収']]
    idnum = 0
    d_nodes = {}
    nodeslist = []
    linkslist = []
    data = {}
    idnum2=0
    blank_d = re.compile('  ')
    blank_d2 = re.compile(' ')
    name_list = ["nodes"]
    colors = ['#F3C759','#C0D860','#5EC84E','#3DB680','#40BFB0','#42AAC7','#44A5CB','#6A8CC7','#8B90BE','#CE579B','#C35B9D','#F9DB57','#FFEE55','#E4EC5B','#45A1CF','#E6855E','#D45D87','#9499C5','#7F96CA','#6C9CCF','#6C9CCF','#6C9CCF','#6C9CCF']

    data["size"] = 150
    data["color"] = '#DA6272'
    data["keyword"] = phrase
    nodeslist.append(data)

    for j,ret_list in enumerate(ret[1:20]):
        dict_sg = {}
        color = colors[j]
        for i,suggest in enumerate(ret_list):
            data = {}
            links = {}
            if i == 0:
                suggest = secondword = suggest[len(phrase):]
                secondword = blank_d.sub('', secondword)
                secondword = blank_d2.sub('', secondword)
                size =60
                links["source"] = 0
                links["target"] = idnum+1
            else:
                pattern = re.compile(phrase)
                pattern2 = re.compile(secondword)
                suggest = pattern.sub('',suggest)
                suggest = pattern2.sub('',suggest)
                size =10
                links["source"] = 1+idnum2
                links["target"] = idnum+1

            if suggest != '':
                idnum += 1
                dict_sg[suggest] = idnum
                data["size"] = size
                data["color"] = color
                data["keyword"] = suggest
                data["number"] = idnum
                nodeslist.append(data)
                linkslist.append(links)
        idnum2 = idnum


    d_nodes["graph"] = []
    d_nodes["links"] = linkslist
    d_nodes["nodes"] = nodeslist
    d_nodes["directed"] = "false"
    d_nodes["multigraph"] = "false"

    fw = open('static/jsonfiles/s_graph.json','w')
    json.dump(d_nodes,fw,ensure_ascii=False,indent=4)
    return
