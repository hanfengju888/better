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
@allure.title('根据qq号查运气')
def test_2():
    allure.attach('''
url:'http://japi.juhe.cn/qqevaluate/qq?qq=1450676007&key=639519cf884578de8e6dce821f4c4175'
headers:
    
body: 

                ''','请求信息') 
    res=requests.request('GET','http://japi.juhe.cn/qqevaluate/qq?qq=1450676007&key=639519cf884578de8e6dce821f4c4175',headers=None,data='',verify=False)
    print(res.json()) 
    allure.attach(json.dumps(res.json(),indent=2,ensure_ascii=False),'响应信息') 
    assert '0' == str(res.json().get('error_code')) 
@allure.title('车辆品牌车型大全')
def test_3():
    allure.attach('''
url:'http://apis.juhe.cn/cxdq/brand?first_letter=A&key=6dd1a438b0e58253589c0773deeac0f2'
headers:
    
body: 

                ''','请求信息') 
    res=requests.request('GET','http://apis.juhe.cn/cxdq/brand?first_letter=A&key=6dd1a438b0e58253589c0773deeac0f2',headers=None,data='',verify=False)
    print(res.json()) 
    allure.attach(json.dumps(res.json(),indent=2,ensure_ascii=False),'响应信息') 
    assert '0' == str(res.json().get('error_code')) 
@allure.title('二十四节气')
def test_4():
    allure.attach('''
url:'http://apis.juhe.cn/fapig/solarTerms/query?year=&name=&key=de1c2b6a738a9590336b3dcae128b812'
headers:
    
body: 

                ''','请求信息') 
    res=requests.request('GET','http://apis.juhe.cn/fapig/solarTerms/query?year=&name=&key=de1c2b6a738a9590336b3dcae128b812',headers=None,data='',verify=False)
    print(res.json()) 
    allure.attach(json.dumps(res.json(),indent=2,ensure_ascii=False),'响应信息') 
    assert '0' == str(res.json().get('error_code')) 
@allure.title('生日书')
def test_5():
    allure.attach('''
url:'http://apis.juhe.cn/fapig/birthdayBook/query?keyword=01-01&key=dcae9f35f96e589efec820b418474d95'
headers:
    
body: 

                ''','请求信息') 
    res=requests.request('GET','http://apis.juhe.cn/fapig/birthdayBook/query?keyword=01-01&key=dcae9f35f96e589efec820b418474d95',headers=None,data='',verify=False)
    print(res.json()) 
    allure.attach(json.dumps(res.json(),indent=2,ensure_ascii=False),'响应信息') 
    assert '0' == str(res.json().get('error_code')) 
@allure.title('每日心灵鸡汤')
def test_6():
    allure.attach('''
url:'https://apis.juhe.cn/fapig/soup/query?key=60399004c84aa9c49bd858255cea0516'
headers:
    
body: 

                ''','请求信息') 
    res=requests.request('GET','https://apis.juhe.cn/fapig/soup/query?key=60399004c84aa9c49bd858255cea0516',headers=None,data='',verify=False)
    print(res.json()) 
    allure.attach(json.dumps(res.json(),indent=2,ensure_ascii=False),'响应信息') 
    assert '0' == str(res.json().get('error_code')) 
@allure.title('随机密码生成器')
def test_7():
    allure.attach('''
url:'http://apis.juhe.cn/fapig/pwdgenerator/generate?len=&t=213&key=adee09e070b26f846f1414b69a5ad190'
headers:
    
body: 

                ''','请求信息') 
    res=requests.request('GET','http://apis.juhe.cn/fapig/pwdgenerator/generate?len=&t=213&key=adee09e070b26f846f1414b69a5ad190',headers=None,data='',verify=False)
    print(res.json()) 
    allure.attach(json.dumps(res.json(),indent=2,ensure_ascii=False),'响应信息') 
    assert '0' == str(res.json().get('error_code')) 
@allure.title('根据qq号查运气')
def test_8():
    allure.attach('''
url:'http://japi.juhe.cn/qqevaluate/qq?qq=1450676007&key=639519cf884578de8e6dce821f4c4175'
headers:
    
body: 

                ''','请求信息') 
    res=requests.request('GET','http://japi.juhe.cn/qqevaluate/qq?qq=1450676007&key=639519cf884578de8e6dce821f4c4175',headers=None,data='',verify=False)
    print(res.json()) 
    allure.attach(json.dumps(res.json(),indent=2,ensure_ascii=False),'响应信息') 
    assert '0' == str(res.json().get('error_code')) 
@allure.title('车辆品牌车型大全')
def test_9():
    allure.attach('''
url:'http://apis.juhe.cn/cxdq/brand?first_letter=A&key=6dd1a438b0e58253589c0773deeac0f2'
headers:
    
body: 

                ''','请求信息') 
    res=requests.request('GET','http://apis.juhe.cn/cxdq/brand?first_letter=A&key=6dd1a438b0e58253589c0773deeac0f2',headers=None,data='',verify=False)
    print(res.json()) 
    allure.attach(json.dumps(res.json(),indent=2,ensure_ascii=False),'响应信息') 
    assert '0' == str(res.json().get('error_code')) 
@allure.title('二十四节气')
def test_10():
    allure.attach('''
url:'http://apis.juhe.cn/fapig/solarTerms/query?year=&name=&key=de1c2b6a738a9590336b3dcae128b812'
headers:
    
body: 

                ''','请求信息') 
    res=requests.request('GET','http://apis.juhe.cn/fapig/solarTerms/query?year=&name=&key=de1c2b6a738a9590336b3dcae128b812',headers=None,data='',verify=False)
    print(res.json()) 
    allure.attach(json.dumps(res.json(),indent=2,ensure_ascii=False),'响应信息') 
    assert '0' == str(res.json().get('error_code')) 
@allure.title('生日书')
def test_11():
    allure.attach('''
url:'http://apis.juhe.cn/fapig/birthdayBook/query?keyword=01-01&key=dcae9f35f96e589efec820b418474d95'
headers:
    
body: 

                ''','请求信息') 
    res=requests.request('GET','http://apis.juhe.cn/fapig/birthdayBook/query?keyword=01-01&key=dcae9f35f96e589efec820b418474d95',headers=None,data='',verify=False)
    print(res.json()) 
    allure.attach(json.dumps(res.json(),indent=2,ensure_ascii=False),'响应信息') 
    assert '0' == str(res.json().get('error_code')) 
@allure.title('每日心灵鸡汤')
def test_12():
    allure.attach('''
url:'https://apis.juhe.cn/fapig/soup/query?key=60399004c84aa9c49bd858255cea0516'
headers:
    
body: 

                ''','请求信息') 
    res=requests.request('GET','https://apis.juhe.cn/fapig/soup/query?key=60399004c84aa9c49bd858255cea0516',headers=None,data='',verify=False)
    print(res.json()) 
    allure.attach(json.dumps(res.json(),indent=2,ensure_ascii=False),'响应信息') 
    assert '0' == str(res.json().get('error_code')) 
@allure.title('随机密码生成器')
def test_13():
    allure.attach('''
url:'http://apis.juhe.cn/fapig/pwdgenerator/generate?len=&t=213&key=adee09e070b26f846f1414b69a5ad190'
headers:
    
body: 

                ''','请求信息') 
    res=requests.request('GET','http://apis.juhe.cn/fapig/pwdgenerator/generate?len=&t=213&key=adee09e070b26f846f1414b69a5ad190',headers=None,data='',verify=False)
    print(res.json()) 
    allure.attach(json.dumps(res.json(),indent=2,ensure_ascii=False),'响应信息') 
    assert '0' == str(res.json().get('error_code')) 
