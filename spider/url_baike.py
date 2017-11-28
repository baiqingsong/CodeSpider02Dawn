#  _*_ coding:utf-8 _*_
import re
import urllib2

url = "https://www.qiushibaike.com/hot/page/1/"
try:
    request = urllib2.Request(url)
    request.add_header('User-Agent', r'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWeb'
                                     r'Kit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36')
    response = urllib2.urlopen(request)
    content = response.read()
    # rs = open("content.html", "w")
    # rs.write(content)
    # pattern = re.compile('<div class="content">\n<span>\n\n\n(.*)\n\n</span>\n\n</div>')
    pattern = re.compile('<a href="/users/\d+/".*?">\n<h2>\n.*?\n</h2>\n</a>')
    items = re.findall(pattern, content)
    for item in items:
        print item, "\n\n"
except urllib2.URLError, e:
    if hasattr(e, 'code'):
        print e.code
    if hasattr(e, 'reason'):
        print e.reason