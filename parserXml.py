#-*- coding:utf-8 -*-__author__ = "苦叶子"# 导入ElementTree
import xml.etree.ElementTree as ET

if __name__ == "__main__":
    print("python xml解析实例")

    data = """
    <data>
        <country name="Liechtenstein">
            <rank>1</rank>
            <year>2008</year>
            <gdppc>141100</gdppc>
            <neighbor name="Austria" direction="E"/>
            <neighbor name="Switzerland" direction="W"/>
        </country>
        <country name="Singapore">
            <rank>4</rank>
            <year>2011</year>
            <gdppc>59900</gdppc>
            <neighbor name="Malaysia" direction="N"/>
        </country>
        <country name="Panama">
            <rank>68</rank>
            <year>2011</year>
            <gdppc>13600</gdppc>
            <neighbor name="Costa Rica" direction="W"/>
            <neighbor name="Colombia" direction="E"/>
        </country>
    </data>
    """
    # 载入xml的两种方式，一种从文件，一种从xml字符串
    # 注意区别：从xml字符串加载的xml直接返回root元素对象
    # 而从文件加载xml返回是xml树

    # 大家根据实际情况来决定用哪种方式即可
    # 本示例从xml字符串载入进行演示

    # 从文件加载xml，获取xml tree节点
    # tree = ET.parse('xml_data.xml')
    
    # 获取根节点
    # root = tree.getroot()

    # 从字符串加载xml
    root = ET.fromstring(data)   
    # 打印下根节点的节点tag， 输出data
    print(root.tag)    
    print("---" * 10)    

    # 遍历下根节点的所有子节点及其属性
    for child in root:
        print(child.tag, " ", child.attrib)    
    print("---" * 10)    
    
    # 找所有的year节点玩下
    for child in root.iter("year"):        
        # 打印出year节点的tag和text
        print(child.tag, " ", child.text)    
    print("---" * 10)    

    # 修改下节点的text试试， 把year节点所有2011修改为2017
    for child in root.iter("year"):        
        if child.text == "2011":
            child.text = "2017"
            child.set('updated', 'yes')    
    print("将2011 改为 2017")    
    
    # 打印下修改后的xml所有的year节点
    for child in root.iter("year"):        
        # 打印出year节点的tag和text
        print(child.tag, " ", child.text)    
    print("---" * 10)    
    
    # 给每个country节点新增一个<wx>开源优测</wx>的节点试试
    for child in root.iter("country"):
        wx = ET.SubElement(child, "wx")
        wx.text = "开源优测"
    
    # 遍历wx节点，并打印
    for child in root.iter("wx"):
        print(child.tag, " ", child.text)    
    print("---" * 10)    

    # 下面演示删除所有的neighbor节点
    # 当然你自己可以加判断条件删除指定的节点，自行尝试吧
    for child in root.findall("neighbor"):
        root.remove(child)    
    # 保存上述操作后的xml至xml_write_data.xml
    xml_update_data = ET.tostring(root, encoding="unicode")   

     # 写入xml_write_data.xml
    import codecs  
    fp = codecs.open("xml_write_data.xml","w","utf-8") 
    
    fp.write(xml_update_data)
    
    fp.close()