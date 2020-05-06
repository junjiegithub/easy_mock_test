"""
    目标：完成登录业务层实现
"""

#导包 unittest ApiLogin
import unittest
from api.api_login import ApiLogin
from parameterized import parameterized
from tools.read_json import ReadJson

#读取数据函数
def get_data():
    data =ReadJson("login.json").read_json()
    #新建空列表，添加读取json数据
    arrs=[]
    arrs.append((data.get("url"),
                data.get("name"),
                data.get("password"),
                data.get("expect_result")
                 ))
    return arrs

#新建测试类
class TestLogin(unittest.TestCase):
    #新建测试方法
    @parameterized.expand(get_data())
    def test_login(self,url,name,password,expect_result):
        #调用登录方法
        s=ApiLogin().api_post_login(url,name,password)

        #调试使用,查看响应结果
        print("查看响应结果",s.json())

        #断言响应信息
        self.assertEqual(expect_result,s.json()['message'])

if __name__ == '__main__':
    unittest.main()


"""
查看响应结果 {'code': 200, 'success': True, 
'message': 'success', 'data': {'_id': '5e9d0bc8e59b590020a44bd4', 
'name': 'easymock01', 'nick_name': '1587350472204',
 'head_img': '//img.souche.com/20161230/png/8bb4f0fd45ed6ae26533eadd85f0f7ea.png', 
 'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjVlOWQwYmM4ZTU5YjU5MDAyMGE0NGJkNCIsImlhdCI6MTU4ODIzNDg0MiwiZXhwIjoxNTg5NDQ0NDQyfQ.12G8f-hPPoTq6P_JgVjq_7rxV9JVnHMQ1vH3zylD4N8'}}
"""
