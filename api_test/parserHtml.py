#-*- coding:utf-8 -*-
__author__ = "苦叶子"

from html.parser import HTMLParser
import http.client

'''
class html.parser.HTMLParser(*, convert_charrefs=True)
1.HTMLParser主要是用来解析HTML文件（包括HTML中无效的标记）
2.参数convert_charrefs表示是否将所有的字符引用自动转化为Unicode形式，
  Python3.5以后默认是True;
3.HTMLParser可以接收相应的HTML内容，并进行解析，
  遇到HTML的标签会自动调用相应的handler（处理方法）来处理，
  用户需要自己创建相应的子类来继承HTMLParser，并且复写相应的handler方法;
4.HTMLParser不会检查开始标签和结束标签是否是一对
'''

class BlogHTMLParser(HTMLParser):
    data = []
    data_key = ""

    def __init__(self):
        HTMLParser.__init__(self)
        self.is_a = False

    def handle_starttag(self, tag, attrs):
        # 处理开始为a的标签
        if tag == "a":
            self.is_a = True
            for name,value in attrs:
                if name == "href":
                    # 提取a的href属性值
                    self.data_key = value    
                    
    def handle_data(self, data):
        # 处理结束为a的标签
        if self.is_a and self.lasttag == "a":                      
            # 将a标签的href属性值作为key， a的文本作为data构建字典
            self.data.append({self.data_key : data})    
    
    def handle_endtag(self, tag):
        # 处理a结束标签
        if self.is_a and self.lasttag == "a":
            self.is_a = False

    def get_data(self):
        # 返回所有从a中提取到的目标数据
        return self.data
                    
    
if __name__ == "__main__":
    print("python HTML解析实例")

    print("访问博客网，获取首页html源码")    
    
    # 构建博客园链接
    conn = http.client.HTTPSConnection("www.cnblogs.com")    
    
    # 获取博客园首页html源码
    conn.request("GET", "/")  
    r1 = conn.getresponse() 
    data = r1.read().decode(encoding="utf-8")    
    # print(data)

    # 解析博客园首页html源码，提取所有a的href和文本数据
    blogHtmlParser = BlogHTMLParser()
    blogHtmlParser.feed(data)
    links = blogHtmlParser.get_data() 
                 
    # 打印提取的结果
    print(links)
'''
HTMLParser常用方法
1.HTMLParser.feed(data)：接收一个字符串类型的HTML内容，并进行解析
2.HTMLParser.close()：当遇到文件结束标签后进行的处理方法。
  如果子类要复写该方法，需要首先调用HTMLParser累的close()
3.HTMLParser.reset():重置HTMLParser实例，该方法会丢掉未处理的html内容
4.HTMLParser.getpos()：返回当前行和相应的偏移量
5.HTMLParser.handle_starttag(tag, attrs)：对开始标签的处理方法。
  例如，参数tag指的是div，attrs指的是一个（name,Value)的列表,这里指(id, main)
6.HTMLParser.handle_endtag(tag)：对结束标签的处理方法。例如，参数tag指的是div
7.HTMLParser.handle_data(data)：对标签之间的数据的处理方法。test,data指的是“test”
8.HTMLParser.handle_comment(data)：对HTML中注释的处理方法。
'''