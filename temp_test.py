# _*_ coding:utf-8 _*_
import pytest,allure,json,requests
@allure.title('添加用户')
def test_0():
    allure.attach('''
url:'https://192.168.4.101/gateway/auth/user/add'
headers:
    {
  "Content-Type": "application/json",
  "requestType": "1",
  "accessToken": "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbiIsInVzZXJuYW1lIjoiYWRtaW4iLCJleHAiOjE2NzIxOTg3ODV9.8acoGlToVwKN7_RVU3c-QtqrmqSVigpWVsCD3EIeahXFsFLh6ShD9va0rj2LN-rSpHyMhhh0VBa5GkeeHUogyQ"
}
body: 
{
  "type": 0,
  "sex": 2,
  "address": [],
  "roleIds": [
    "1"
  ],
  "expireTime": "",
  "periodType": 1,
  "dataPermissionType": 2,
  "username": "han16690231474662",
  "password": "1qaz@WSX",
  "nickname": "hanuser16690234174662",
  "email": "123@qq.com",
  "phone": "17600000000",
  "deptIds": [
    1
  ],
  "dataPermissionDepts": []
}
                ''','请求信息') 
    res=requests.request('POST','https://192.168.4.101/gateway/auth/user/add',headers={"Content-Type":"application/json","requestType":"1","accessToken":"eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbiIsInVzZXJuYW1lIjoiYWRtaW4iLCJleHAiOjE2NzIxOTg3ODV9.8acoGlToVwKN7_RVU3c-QtqrmqSVigpWVsCD3EIeahXFsFLh6ShD9va0rj2LN-rSpHyMhhh0VBa5GkeeHUogyQ"},data='{"type":0,"sex":2,"address":[],"roleIds":["1"],"expireTime":"","periodType":1,"dataPermissionType":2,"username":"han16690231474662","password":"1qaz@WSX","nickname":"hanuser16690234174662","email":"123@qq.com","phone":"17600000000","deptIds":[1],"dataPermissionDepts":[]}',verify=False)
    print(res.json()) 
    allure.attach(json.dumps(res.json(),indent=2,ensure_ascii=False),'响应信息') 
    assert '200' == res.json()['data']['code'] 
@allure.title('解锁用户')
def test_1():
    allure.attach('''
url:'https://192.168.4.101/gateway/auth/user/disable/user?status=0&userId=8'
headers:
    {
  "Content-Type": "application/json",
  "requestType": "1",
  "accessToken": "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbiIsInVzZXJuYW1lIjoiYWRtaW4iLCJleHAiOjE2NzIxOTg3ODV9.8acoGlToVwKN7_RVU3c-QtqrmqSVigpWVsCD3EIeahXFsFLh6ShD9va0rj2LN-rSpHyMhhh0VBa5GkeeHUogyQ"
}
body: 

                ''','请求信息') 
    res=requests.request('POST','https://192.168.4.101/gateway/auth/user/disable/user?status=0&userId=8',headers={"Content-Type":"application/json","requestType":"1","accessToken":"eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbiIsInVzZXJuYW1lIjoiYWRtaW4iLCJleHAiOjE2NzIxOTg3ODV9.8acoGlToVwKN7_RVU3c-QtqrmqSVigpWVsCD3EIeahXFsFLh6ShD9va0rj2LN-rSpHyMhhh0VBa5GkeeHUogyQ"},data='',verify=False)
    print(res.json()) 
    allure.attach(json.dumps(res.json(),indent=2,ensure_ascii=False),'响应信息') 
    assert '200' == res.json()['data']['code'] 
