import pytest
import yaml

from pytestcode.cal import Calculater

@pytest.fixture()
def testcal():
    cal = Calculater()
    print("开始计算")
    yield cal
    print("结束计算")

def pytest_addoption(parser):
    mygroup = parser.getgroup("myenv")
    mygroup.addoption("--env",
                      default="test",
                      dest='env',
                      help="my env")

@pytest.fixture()
def cmdoption(request):
    menv = request.config.getoption("--env", default="test")
    if menv == "test":
        print("这是测试环境")
        with open("../datas/test.yml", 'rb') as f:
            datas = yaml.safe_load(f)
    elif menv == "dev":
        print("这是开发环境")
        with open("../datas/dev.yml", 'rb') as f:
            datas = yaml.safe_load(f)
    elif menv == "st":
        print("这是st环境")
        with open("../datas/st.yml", 'rb') as f:
            datas = yaml.safe_load(f)
    return datas
