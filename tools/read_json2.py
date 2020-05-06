#导包json

import  json

#新建读取类
class ReadJson(object):
    #新建方法，读取文件地址
    def __init__(self,filename):
        self.filepath=("/Users/junjie/PycharmProjects/easy_mock_test/data/"+filename)

    #新建方法，加载文件流
    def read_json(self):
        with open(self.filepath,"r",encoding="utf-8") as f:
            #调用load方法加载文件流
            return json.load(f)

if __name__ == '__main__':
    #data =ReadJson("login2.json").read_json()
    data =ReadJson("create.json").read_json()
    print(data)
    #新建空列表，添加读取json的数据
    arrs=[]
    arrs.append((data.get('url'),
                 data.get('headers'),
                 data.get('data'),
                 data.get('expect_result')
                 ))
    print(arrs)