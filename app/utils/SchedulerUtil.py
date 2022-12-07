import datetime
import time

from flask_apscheduler import APScheduler
import os

import app
from app.models import db
from app.models.job import Job
from app.models.project import Project
from app.models.project_scheduler import ProjectScheduler
from app.models.project_test_case import ProjectTestCase
from app.utils.GeneratePyTestCaseUtil import GeneratePyTestCase
from app.utils.executor import Executor
from config import Config

scheduler = APScheduler()


# @scheduler.task('interval', id='do_job_1', seconds=4, misfire_grace_time=900)
# def job1():
#     print('Job 1 executed')

def execute_cases_by_project_id(project_id,project_scheduler_id):
    #更新定时任务表中执行次数
    update_p = ProjectScheduler.query.get(project_scheduler_id)
    update_p.execute_count += 1
    db.session.commit()

    project_test_cases = ProjectTestCase.query.filter(ProjectTestCase.project_id == project_id,ProjectTestCase.deleted_at == None).all()
    name = "scheduler_" + str(int(time.time()))
    job_path = os.path.join(Config.TESTCASE_REPORT_PATH,name)
    if not os.path.exists(job_path):
        os.makedirs(job_path)
    py_path = os.path.join(job_path, 'temp_test.py')
    f = open(py_path, 'w+', encoding='utf-8')
    f.writelines('# _*_ coding:utf-8 _*_\n')
    f.writelines('import pytest,allure,json,requests\n')

    num = 0
    id_list = []
    for project_test_case in project_test_cases:
        id_list.append(project_test_case.id)
        GeneratePyTestCase.generate_pytest_testcase(project_test_case.id, num, f)
        num += 1

    f.close()

    print(job_path)

    # 存入任务到数据库
    allure_report_path = os.path.join(job_path, 'allure_report')

    inser_job = Job(int(project_id), str(id_list), name, len(id_list),allure_report_path)
    db.session.add(inser_job)
    db.session.commit()



    # 执行命令
    # pytest xx.py --alluredir=report
    # allure generate ./allure-results/ -o ./allure-report/
    # allure open -h 127.0.0.1 -p 8080 ./allure-report/
    def execute_job():
        update_job = Job.query.get(inser_job.id)
        st = time.time()
        os.system(f"pytest {py_path} --alluredir={os.path.join(job_path, 'pytest_report')}")
        os.system(
            f"allure generate {os.path.join(job_path, 'pytest_report')}/ -o {os.path.join(job_path, 'allure_report')} ")
        how_long = round(time.time() - st)
        update_job.how_long = how_long
        update_job.end_at = datetime.datetime.now()
        update_job.status = '2'

        db.session.commit()

    Executor.thread_run(execute_job)
