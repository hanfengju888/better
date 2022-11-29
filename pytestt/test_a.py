import pytest
import allure
def setup_module():
    print("setup_function....")

def teardown_module():
    print("this is teardown....")

@allure.title('添加用户')
def test_ooone():
    print("this is test_one")
    allure.attach('URL:https://www.baidu.com \n 请求头:{"Content-Type":"application/json"}', '请求信息:')
    assert 1 == 2

@allure.title('删除用户')
def test_two():
    print("this is test_two")
    assert 1 ==1

@pytest.mark.skip
def test_skip():
    print("this is skip")

if __name__ == "__main__":
    pytest.main(['-s','-q','--alluredir','./report'])