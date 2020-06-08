#encoding:utf8
import time
#1、导入包
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
#2、desired创建字典
desired_caps=dict()
#3、platformName
desired_caps['platformName'] = 'Android'
#4、platformVersion
desired_caps['platfromVersion']='8.0'
#5、deviceName
desired_caps['deviceName'] = 'Google'

#6、启动程序的包名appPackage
#计算器 com.android.calculator2/com.android.calculator2.Calculator
#设置 com.android.settings/com.android.settings.Settings}

desired_caps["appPackage"] = 'com.boxuegu'
#desired_caps["appPackage"] = 'com.android.calculator2'
#desired_caps["appPackage"] = 'com.android.settings'
#desired_caps["appPackage"] = 'com.android.email'
#7、启动界面名appActivity
desired_caps['appActivity'] = 'com.boxuegu.activity.MainFlutterActivity'
#desired_caps['appActivity'] = 'com.android.calculator2.Calculator'#
#desired_caps['appActivity'] = 'com.android.settings.Settings'
#desired_caps['appActivity'] = 'com.android.email.activity.setup.AccountSetupFinal'

#解决中文
desired_caps["unicodeKeyboard"] = True
desired_caps["resetKeyboard"] = True

#获取toast automationName = uiautomator2
desired_caps["automationName"] = 'uiautomator2'
#8、http，连接appium服务器
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
time.sleep(5)
#显示等待
allow_btn = WebDriverWait(driver,2,0.5).until(lambda x:x.find_element_by_id("com.android.packageinstaller:id/permission_allow_button"))

#1、定位允许按钮
#allow_btn = driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
#2、点击操作1
allow_btn.click()
time.sleep(5)
#driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
WebDriverWait(driver,2,0.5).until(lambda x:x.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")).click()

time.sleep(5)
#1、点击我的 id、class、xpath
me = '//*[starts-with(@text,"我的")]'
driver.find_element_by_xpath(me).click()
time.sleep(5)
#2、输入用户名
username="com.boxuegu:id/edit_usr"
driver.find_element_by_id(username).send_keys("13133")
time.sleep(2)
#3、输入验证码
code = "com.boxuegu:id/security_code"
driver.find_element_by_id(code).send_keys("131")
time.sleep(2)
#4、点击登录
login_btn="com.boxuegu:id/btn_login"
driver.find_element_by_id(login_btn).click()

#5、获取toast信息
toast=WebDriverWait(driver,5).until(lambda x:x.find_element_by_xpath("//*[contains(@text,'手机号格式错误')]"))
print(toast.text)