# __*__ encoding:utf-8 __*__

from taobao_girl import html_downloader, html_manager, html_parser, html_output
from taobao_girl.tool import Tool


class TaobaoGirl(object):

    def __init__(self, site_url):
        self.site_url = site_url
        self.urls = html_manager.HtmlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.output = html_output.HtmlOutput()
        self.tool = Tool()

    def savePageInfo(self, url):
        # 获取网页内容
        page = self.downloader.download(url)
        # 获取一页淘宝MM列表
        contents = self.parser.get_content(page)
        for item in contents:
            # item[0]个人详情URL,item[1]头像URL,item[2]姓名,item[3]年龄,item[4]居住地
            print u"发现一位模特,名字叫", item[2], u"芳龄", item[3], u",她在", item[4]
            print u"正在偷偷地保存", item[2], "的信息"
            print u"又意外地发现她的个人地址是", item[0]
            # 个人详情页面
            detailPage = self.downloader.download(item[0])
            # 个人简介
            brief = self.parser.get_brief(detailPage)
            # 获取所有图片列表
            images = self.parser.get_all_img(detailPage)
            # 创建文件夹
            self.output.mkdir(item[2])
            # 保存个人简历
            self.output.save_brief(brief, item[2])
            # 保存头像
            self.output.save_icon(item[1], item[2])
            # 保存多张图片
            self.output.save_imgs(images, item[2])
            print item[2] + u"的信息保存完毕"

    def savePagesInfo(self, start, end):
        for i in range(start, end + 1):
            print u"正在偷偷寻找第", i, u"个地方，看看MM们在不在"
            self.savePageInfo(self.site_url + "?page=" + str(i))


if __name__ == "__main__":
    taobaoGirl = TaobaoGirl("https://mm.taobao.com/json/request_top_list.htm")
    taobaoGirl.savePagesInfo(1, 1)