# __*__ encoding:utf-8 __*__
import re

from taobao_girl.tool import Tool


class HtmlParser(object):

    def __init__(self):
        self.tool = Tool()

    # 获取索引页面所有MM信息，list格式
    def get_content(self, page):
        pattern = re.compile(
            '<div class="list-item".*?<a href="(.*?)".*?<img src="(.*?)".*?<a class="lady-name.*?>(.*?)</a>'
            '.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>',
            re.S)
        items = re.findall(pattern, page)
        contents = []
        for item in items:
            contents.append(["http:" + item[0], "http:" + item[1], item[2], item[3], item[4]])
        return contents

    # 获取个人文字简介
    def get_brief(self, page):
        pattern = re.compile('<div class="mm-aixiu-content".*?>(.*?)<!--',re.S)
        try:
            result = re.search(pattern, page)
            if result:
                return self.tool.replace(result.group(1))
        except:
            print "get brief error "

    # 获取页面所有图片
    def get_all_img(self, page):
        imageUrls = []
        pattern = re.compile('<div class="mm-aixiu-content".*?>(.*?)<!--',re.S)
        try:
            result = re.search(pattern, page)
            if result is None:
                return None
            pattern_img = re.compile('<img.*?src="(.*?)"',re.S)
            images = re.findall(pattern_img, result.group(1))
            for image in images:
                imageUrls.append("http:" + image)
            return imageUrls
        except:
            print "get all images error"