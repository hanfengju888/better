import json

from app.dao.testcase.TestCaseDao import TestCaseDao


class GeneratePyTestCase():
    @staticmethod
    def generate_pytest_testcase(id,num,f):
        case_info, err = TestCaseDao.query_case_by_id(id)
        headers = case_info.request_header
        url = case_info.url
        data = '' if case_info.body is None else case_info.body
        data = data.replace('\n', '').replace(' ', '').replace('\r', '')
        method = case_info.request_method
        expected = case_info.expected
        attach_info_headers = '' if headers == None else json.dumps(json.loads(headers), indent=2, ensure_ascii=False)
        attach_info_body = "" if data == "" else json.dumps(json.loads(data), indent=2, ensure_ascii=False)

        attach_info = f'''
url:'{url}'
headers:
    {attach_info_headers}
body: 
{attach_info_body}
                '''

        f.writelines(f"@allure.title('{case_info.name}')\n")
        f.writelines(f'def test_{num}():\n')
        f.writelines(f"    allure.attach('''{attach_info}''','请求信息') \n")

        f.writelines(f"    res=requests.request('{method}','{url}',headers={headers},data='{data}',verify=False)\n")
        f.writelines(f"    print(res.json()) \n")

        f.writelines(f"    allure.attach(json.dumps(res.json(),indent=2,ensure_ascii=False),'响应信息') \n")
        f.writelines(f"    assert '{expected}' == str(res.json().get('error_code')) \n")
