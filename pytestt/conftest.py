def pytest_collectstart(collector):
    print("开始收集用例。。")

def pytest_itemcollected(item):
    print(item)