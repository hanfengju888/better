# _*_ coding:utf-8 _*_
import pytest,allure,json,requests
@allure.title('qq号查运气')
def test_0():
    allure.attach('''
url:'http://japi.juhe.cn/qqevaluate/qq?qq=1450676007&key=639519cf884578de8e6dce821f4c4175'
headers:
    
body: 

                ''','请求信息') 
    res=requests.request('GET','http://japi.juhe.cn/qqevaluate/qq?qq=1450676007&key=639519cf884578de8e6dce821f4c4175',headers=None,data='',verify=False)
    print(res.json()) 
    allure.attach(json.dumps(res.json(),indent=2,ensure_ascii=False),'响应信息') 
    assert '' == res.json().get('error_code') 
