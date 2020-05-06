"""
    实现创建项目接口封装

"""

#导包requests
import requests

#新建创建项目类
class ApiCreate(object):
    #新建创建项目方法
    def api_post_create(self,url,headers,data):
        #调用post方法，并返回响应对象
        return requests.post(url,headers=headers,json=data)


