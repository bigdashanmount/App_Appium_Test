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
#8、http，连接appium服务器
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

#time.sleep(5)
#隐式等待 driver.implicitly_wait(5)

#显示等待
allow_btn = WebDriverWait(driver,2,0.5).until(lambda x:x.find_element_by_id("com.android.packageinstaller:id/permission_allow_button"))

#1、定位允许按钮
#allow_btn = driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
#2、点击操作1
allow_btn.click()



#1、获取包和activity
#com.android.email/com.android.email.activity.setup.AccountSetupFinal
#2、获取元素定位
#id com.android.email:id/account_email
#account_email = driver.find_element_by_id("com.android.email:id/account_email")
#3、输入操作
#send_keys
#account_email.send_keys("你好")
#time.sleep(2)
#account_email.clear()

#获取元素内容
#text
#account_text = account_email.text
#print(account_text)

#获取元素属性
#account_attr = account_email.get_attribute("text")
#print(account_attr)
#account_attr_package = account_email.get_attribute("package")
#print(account_attr_package)

#打印当前包名
#print(driver.current_package)

#打印当前界面名
#print(driver.current_activity)

#关闭app
#driver.close_app()
#启动
#driver.launch_app()
time.sleep(10)

#退出driver
driver.quit()

#不能放在quit()方法后执行相关操作driver.launch_app()