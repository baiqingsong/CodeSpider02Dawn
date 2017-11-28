#  _*_ coding:utf-8 _*_
import re
import urllib2


# 处理页面标签类
class Tool:
    # 去除img标签,7位长空格
    removeImg = re.compile('<img.*?>| {7}|')
    # 删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')
    # 把换行的标签换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    # 将表格制表<td>替换为\t
    replaceTD = re.compile('<td>')
    # 把段落开头换为\n加空两格
    replacePara = re.compile('<p.*?>')
    # 将换行符或双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')
    # 将其余标签剔除
    removeExtraTag = re.compile('<.*?>')

    def replace(self, x):
        x = re.sub(self.removeImg, "", x)
        x = re.sub(self.removeAddr, "", x)
        x = re.sub(self.replaceLine, "\n", x)
        x = re.sub(self.replaceTD, "\t", x)
        x = re.sub(self.replacePara, "\n    ", x)
        x = re.sub(self.replaceBR, "\n", x)
        x = re.sub(self.removeExtraTag, "", x)
        # strip()将前后多余内容删除
        return x.strip()


class BDTB:
    # 初始化，传入基参数
    def __init__(self, baseUrl, seelZ):
        self.baseUrl = baseUrl
        self.seelZ = "?see_lz=" + str(seelZ)
        self.tool = Tool()

    def getPage(self, pageNum=1):
        try:
            url = self.baseUrl + self.seelZ + "&pn=" + str(pageNum)
            print url
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            # print response.read()
            return response.read()
        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print "连接百度链接失败，错误原因", e.reason
                return None

    def getTitle(self, content):
        pattern = re.compile('<h3 class="core_title_txt.*?>(.*?)</h3>')
        result = re.search(pattern, content)
        if result:
            return result.group(1).strip()
        else:
            return None

    def getPageNum(self, content):
        pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>', re.S)
        result = re.search(pattern, content)
        if result:
            return result.group(1).strip()
        else:
            return None

    def getContent(self, page):
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>', re.S)
        items = re.findall(pattern, page)
        floor = 1
        for item in items:
            print floor, u"楼------------------------------------------------------------------------------------------------------------------------------------\n"
            print self.tool.replace(item)
            floor += 1


bdtb = BDTB("http://tieba.baidu.com/p/3138733512", 1)
print bdtb.getPageNum(bdtb.getPage(1))