# _*_ coding:utf-8 _*_
import pytest,allure,json,requests
@allure.title('查询成语')
def test_0():
    allure.attach('''
url:'http://apis.juhe.cn/idioms/query?wd=%E4%B8%80%E5%BF%83%E4%B8%80%E6%84%8F&key=3fc2a87f21c1e85310239fc6be4ec120'
headers:
    
body: 

                ''','请求信息') 
    res=requests.request('GET','http://apis.juhe.cn/idioms/query?wd=%E4%B8%80%E5%BF%83%E4%B8%80%E6%84%8F&key=3fc2a87f21c1e85310239fc6be4ec120',headers=None,data='',verify=False)
    print(res.json()) 
    allure.attach(json.dumps(res.json(),indent=2,ensure_ascii=False),'响应信息') 
    assert '0' == str(res.json().get('error_code')) 
@allure.title('查询北京天气预报')
def test_1():
    allure.attach('''
url:'http://v.juhe.cn/weather/index?cityname=%E5%8C%97%E4%BA%AC&dtype=1&format=1&key=d86395eed492ec3f286f16bee8a648de'
headers:
    
body: 

                ''','请求信息') 
    res=requests.request('GET','http://v.juhe.cn/weather/index?cityname=%E5%8C%97%E4%BA%AC&dtype=1&format=1&key=d86395eed492ec3f286f16bee8a648de',headers=None,data='',verify=False)
    print(res.json()) 
    allure.attach(json.dumps(res.json(),indent=2,ensure_ascii=False),'响应信息') 
    assert '0' == str(res.json().get('error_code')) 
