#导包

import unittest
from api.api_create import ApiCreate
from parameterized import parameterized
from tools.read_json import ReadJson

def get_data_create():
    data=ReadJson("create.json").read_json()
    #新建空列表，添加读取json数据
    arrs=[]
    arrs.append((data.get("url"),
                data.get('headers'),
                data.get('expect_result'),
                data.get('data')))
    return arrs

#新建测试类 继承
class TestCreate(unittest.TestCase):
    #新建创建项目方法
    @parameterized.expand(get_data_create())
    def test_create(self,url,headers,data,expect_result):
        #调用创建项目方法
        r=ApiCreate().api_post_create(url,headers,data)

        print("创建项目响应数据为",r.content)
        # 使用动态数据获取 响应信息
        self.assertEquals(expect_result, r.json()["message"])


if __name__ == '__main__':
    unittest.main()