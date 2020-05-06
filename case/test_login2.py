"""
    完成登录业务层的实现
"""

#导包 unittest，ApiLogin
import unittest
from api.api_login import ApiLogin
from parameterized import parameterized
from tools.read_json import ReadJson

#新建读取数据函数方法
def get_data():
    data =ReadJson("login.json").read_json()
    #新建空列表，存放读取json数据
    arrs =[]
    arrs.append((data.get('url'),
                 data.get('name'),
                  data.get('password'),
                   data.get('expect_result'))
                 )
    return arrs

#新建测试类
class Test_Login(unittest.TestCase):
    @parameterized.expand(get_data())
    #新建测试方法
    def test_login(self,url,name,password,expect_result):
        #调用登录方法
        s=ApiLogin().api_post_login(url,name,password)
        #调试使用，查看响应结果
        print('查看响应结果',s.json())
        #断言响应结果
        self.assertEqual(expect_result,s.json()['message'])


if __name__ == '__main__':
    unittest.main()
