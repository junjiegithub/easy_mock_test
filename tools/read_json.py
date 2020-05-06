#导包 json

import json

#新建读取类
class ReadJson(object):

    def __init__(self,filename):
        self.filepath ="/Users/junjie/PycharmProjects/easy_mock_test/data/"+filename

    def read_json(self):
        with open(self.filepath,"r",encoding="utf-8") as f:
            #调用load方法加载文件流
            return json.load(f)

if __name__ == '__main__':
    #print(ReadJson("login.json").read_json())
    data = ReadJson("login.json").read_json()
    # 新建空列表，添加读取json数据
    arrs = []
    arrs.append((data.get("url"),
                 data.get("name"),
                 data.get("password"),
                 data.get("expect_result")
                 ))
    print(arrs)