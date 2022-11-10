from collections import defaultdict

from app.models.test_case import TestCase
from app.utils.logger import Log

class TestCaseDao(object):
    log = Log("TestCaseDao")

    @staticmethod
    def list_test_case(project_id):
        try:
            case_list = TestCase.query.filter_by(project_id=project_id,deleted_at=None).order_by(TestCase.name.asc()).all()
            return TestCaseDao.get_tree(case_list),None
        except Exception as e:
            TestCaseDao.log.error(f"获取测试用例失败:{str(e)}")
            return [],f"获取测试用例失败:{str(e)}"

    @staticmethod
    def get_tree(case_list):
        result = defaultdict(list)
        #获取目录 -> 用例的映射关系
        for cs in case_list:
            result[cs.catalogue].append(cs)
        keys = sorted(result.keys())
        tree = [dict(key=f"cat_{key}",
                     children=[{"key": f"case_{child.id}", "title": child.name} for child in result[key]],
                     title=key, total=len(result[key])) for key in keys]

    @staticmethod
    def query_case_by_id(case_id):
        try:
            tc = TestCase.query.filter_by(id=case_id,deleted_at=None).first()
            return tc,None
        except Exception as e:
            err = f"TestCaseDao: 查询用例失败，{str(e)}"
            TestCaseDao.log.error(err)
            return None,err




