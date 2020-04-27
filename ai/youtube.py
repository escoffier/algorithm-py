# -*- coding: utf-8 -*-
import urllib
import requests
import json
import execjs

VIDEO_ID = 'TJFG1194O4Y'
START_TOKEN = 'ytplayer.config = '
END_TOKEN = ';ytplayer.load'

def convert_to_dict(data):
    result = {}
    list = data.split('&')
    for item in list:
        pair = item.split('=')
        key = urllib.unquote_plus(pair[0])
        value = urllib.unquote_plus(pair[1])
        result[key] = value
    return result

def parse_js(data):
    start = data.find(b"""a.splice(0,b)""")
    start = data.rfind(b";var", 0 , start)
    end = data.find(b"""return a.join("")};""", start)
    js = data[start:end+len(b"""return a.join("")};""")]
    start = js.find(b"""function """)
    end = js.find(b"""(a)""" , start)
    name = js[start+len(b"""function """):end]
    return name, js


if __name__ == '__main__':
    print("Using javascript interpreter:", execjs.get().name)
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36',
               'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.6,en;q=0.4',
               'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
               'Accept-Encoding': 'gzip, deflate, sdch'}
    response = requests.get("https://www.youtube.com/watch?v=%s" % VIDEO_ID, headers=headers)
    data = response.content
    start = data.find(bytearray(START_TOKEN, encoding='utf-8'))
    end = data.find(bytearray(END_TOKEN, encoding='utf-8'))
    data = data[start+len(START_TOKEN):end]
    data = json.loads(data)

    js = 'https://www.youtube.com' + data['assets']['js']
    response = requests.get(js)
    jscontent = response.content
    func, jscontent = parse_js(jscontent)
ctxt = execjs.compile(jscontent)

    data = data['args']
    # print("Title:", data['title'])
    list = data['adaptive_fmts'].split(',')
    parsed = []
    for item in list:
        info = convert_to_dict(item)
        if info['url'].find("&signature=") == -1:
            info['url'] = info['url'] +"&signature=" + ctxt.call(func, info['s'])
        parsed.append(info)

    for item in parsed:
        if item['type'].startswith("video"):
            print ("%-35s|%-10s%2sfps|%-10s|%s" % (item['type'], item['size'], item['fps'], "%0.2fMiB" % (float(item['clen'])/1024/1024), item['url']))
        else:
            print("%-35s|%-10s%5s|%-10s|%s" % (item['type'], ""          , ""         , "%0.2fMiB" % (float(item['clen'])/1024/1024), item['url']))