# __*__ encoding:utf-8 __*__
import urllib

import os
import urllib2


class HtmlOutput(object):
    def output_html(self, new_data):
        pass

    # 创建新目录
    def mkdir(self, path):
        path = path.strip()
        isExists = os.path.exists(path)
        if not isExists:
            print u"偷偷新建了名字叫做", path, u'的文件夹'
            os.mkdir(path)
            return True
        else:
            print u"名为", path, '的文件夹已经创建成功'
            return False

    # 传入文件地址，文件名，保存单张图片
    def save_img(self, imgUrl, fileName):
        if imgUrl is None:
            return None
        f = open(fileName, "wb")
        try:
            u = urllib2.urlopen(imgUrl)
            data = u.read()
            f.write(data)
            print u"正在悄悄保存她的一张图片为", fileName
        except:
            print "save image error = " + fileName
        finally:
            f.close()

    # 保存多张图片
    def save_imgs(self, images, name):
        if images is None:
            return None
        number = 1
        print u"发现", name, u"共有", len(images), u"张照片"
        for imgUrl in images:
            splitPath = imgUrl.split('.')
            # 删除最后一项并且返回
            fTail = splitPath.pop()
            if len(fTail) > 3:
                fTail = "jpg"
            fileName = name + "/" + str(number) + "." + fTail
            self.save_img(imgUrl, fileName)
            number += 1

    # 保存头像
    def save_icon(self, iconUrl, name):
        if iconUrl is None:
            return None
        splitPath = iconUrl.split('.')
        fTail = splitPath.pop()
        fileName = name + "/icon." + fTail
        self.save_img(iconUrl, fileName)

    # 保存个人信息
    def save_brief(self, content, name):
        if content is None:
            return None
        fileName = name + "/" + name + ".txt"
        f = open(fileName, "w+")
        print u"正在偷偷保存她的个人信息为", fileName
        f.write(content.encode('utf-8'))