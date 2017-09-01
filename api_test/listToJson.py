#-*- coding:utf-8 -*-
#__author__ = "苦叶子"

import json

if __name__ == "__main__":
    print("python json标准库解析实例")

    # python对象转json对象
    raw_data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]


    # 打印出来看下效果
    print("转化前,python")
    print(type(raw_data))
    print(raw_data)
    print("-" * 40)

	# json.dumps 将Python对象编码成json字符串
    # json_data = json.dumps(raw_data)
    # 把json串进行格式化
    json_data = json.dumps(raw_data, 
    	sort_keys=True, 
    	indent=4, 
    	separators=(',', ': '))

    print("转化后,json")
    print(type(json_data))
    print(json_data)
    print("-" * 40)

    # 将json对象转化成python对象
    print("将json对象转化成python对象")
    # json.loads 将已编码的json字符串解码为Python对象
    python_data = json.loads(json_data)
    print(type(python_data))
    print(python_data)