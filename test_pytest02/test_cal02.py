"""
课后作业1
1、使用参数化数据驱动，完成加减乘除测试用例的自动生成
2、修改测试用例为check_开头，修改测试用例的执行规则，执行所有check_开头和test_开头的测试用例
课后作业2
控制测试用例顺序按照【加-减-乘-除】这个顺序执行,
减法依赖加法， 除法依赖乘法
课后作业3
注册一个命令行参数env,env默认值是test,表示测试环境，另外还有两个值 （dev,st）不同的环境读取不同的数据。
"""
import pytest
import yaml

class TestCal:

    @pytest.mark.parametrize("a, b, result", yaml.safe_load(open("../datas/cal_data.yml", "rb"))["add"],
                             ids=["int", "bignum", "float", "negative"])
    @pytest.mark.run(order=1)
    @pytest.mark.dependency(name="add")
    def check_add(self, testcal, a, b, result):
        assert result == testcal.add(a, b)

    @pytest.mark.parametrize("a, b, result", yaml.safe_load(open("../datas/cal_data.yml", "rb"))["sub"],
                             ids=["int", "bignum", "float", "negative"])
    @pytest.mark.run(order=2)
    @pytest.mark.dependency(depends=["add"])
    def check_sub(self, testcal, a, b, result):
        assert result == testcal.sub(a, b)

    @pytest.mark.parametrize("a, b, result", yaml.safe_load(open("../datas/cal_data.yml", "rb"))["mul"],
                             ids=["int", "bignum", "float", "negative"])
    @pytest.mark.run(order=3)
    @pytest.mark.dependency(name="mul")
    def check_mul(self, testcal, a, b, result):
        assert result == testcal.mul(a, b)

    @pytest.mark.parametrize("a, b, result", yaml.safe_load(open("../datas/cal_data.yml", "rb"))["div"],
                             ids=["int", "bignum", "float", "negative", "div=0"])
    @pytest.mark.run(order=4)
    @pytest.mark.dependency(depends=["mul"])
    def check_div(self, testcal, a, b, result):
        if b == 0:
            print("除数不能为0")
        else:
            assert result == testcal.div(a, b)
