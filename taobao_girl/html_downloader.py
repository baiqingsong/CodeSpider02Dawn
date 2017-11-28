# __*__ encoding:utf-8 __*__
import urllib2


class HtmlDownloader(object):

    def download(self, new_url):
        request = urllib2.Request(new_url)
        request.add_header('user-agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36')
        request.add_header('cookie', 'miid=1438969084677917634; thw=cn; UM_distinctid=15eecb525cc241-010d7131a3599f-3e63430c-15f900-15eecb525cd4ec; cna=oZGpEfrk6X8CAdpQ3TyyNh1z; l=AqCgHaGPqkNyVTFXgp/GIBZ/8KRyo4Rz; CNZZDATA30064598=cnzz_eid%3D922122902-1511775272-https%253A%252F%252Fmm.taobao.com%252F%26ntime%3D1511844955; CNZZDATA30063600=cnzz_eid%3D1757041768-1511778900-https%253A%252F%252Fmm.taobao.com%252F%26ntime%3D1511844955; _tb_token_=fb1ea08db3bef; hng=CN%7Czh-CN%7CCNY%7C156; v=0; swfstore=82159; uc3=sg2=W5oAJC5dYpgc%2BxomAZjeCLjSTvfYPtDWNxOwNkPQbhg%3D&nk2=odahvL1xe6s%3D&id2=UNX4F9wg3iP7Ig%3D%3D&vt3=F8dBzLQH4K3%2B1A1G27s%3D&lg2=W5iHLLyFOGW7aA%3D%3D; existShop=MTUxMTg4Mjk4Mw%3D%3D; uss=ACzgsEI7EVNPy8kzSqn586U4lt0tCA2Jng825CJQMp30qpSnZdq6mCbd; lgc=%5Cu5988%5Cu5988dawn; tracknick=%5Cu5988%5Cu5988dawn; cookie2=12273659434f76fc4e1cab5de993a46a; sg=n1e; mt=np=&ci=0_1; cookie1=VW8XtlqIQYNq9zrQoIJHrponoxXWXrzbUZ%2BdT5WpZUA%3D; unb=3533827871; skt=c05bf7594953472a; t=cb9dbd0af8e28b07ac9b462c8b230b0b; _cc_=V32FPkk%2Fhw%3D%3D; tg=5; _l_g_=Ug%3D%3D; _nk_=%5Cu5988%5Cu5988dawn; cookie17=UNX4F9wg3iP7Ig%3D%3D; JSESSIONID=6B8CDE70866C266B125A01D3C1C7BD92; uc1=cookie14=UoTdevRwdyXlDA%3D%3D&lng=zh_CN&cookie16=URm48syIJ1yk0MX2J7mAAEhTuw%3D%3D&existShop=false&cookie21=VT5L2FSpdiBh&tag=8&cookie15=VT5L2FSpMGV7TQ%3D%3D&pas=0; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; isg=Anp6kem99Ogik3uuDG0w3lrjy6Bcg5tW6Nds_oRzJo3YdxqxbbtOFUCNsTRR; whl=-1%260%260%261511883404799')
        request.add_header('accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8')
        try:
            response = urllib2.urlopen(request)
            if response.getcode() != 200:
                return None
            return response.read().decode('gbk')
        except:
            print "get url fail " + new_url
