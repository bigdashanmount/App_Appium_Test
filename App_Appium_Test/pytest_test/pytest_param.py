import pytest

#单个参数
#1、定义一个测试用例方法
name_list = ["小红","小明"]
@pytest.mark.parametrize("name",name_list)
def test_a(name):
    print(name)
#2、一个参数进行参数化


#多个参数
name_password_list=[("xiaoming","123123"),("xiaohong","456456")]
@pytest.mark.parametrize(("name","password"),name_password_list)
def test_b(name,password):
    print(name)
    print(password)

#字典
login_list=[{"username":"xiaoming","password":"123123"},{"username":"xiaohong","password":"456456"}]
@pytest.mark.parametrize("login",login_list)
def test_c(login):
    print(login)



if __name__ == '__main__':
    pytest.main(["-s", "pytest_param.py", "--html=移动端自动化测试报告.html"])
