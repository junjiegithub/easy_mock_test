"""
    实现登录接口封装
"""

#导包 requests
import requests

#新建类，登录接口对象
class ApiLogin(object):
    #新建方法，登录方法
    def api_post_login(self,url,name,password):
        #headers的定义
        headers ={"Content-Type":"application/json"}
        #data的定义
        data={"name":name,"password":password}
        #调用post并返回响应对象
        return requests.post(url,headers=headers,json=data)

"""
提示：
    url，name,password:最后都需要从data数据文件中，读取出来，做参数化使用，所以这里选择动态传参
"""



