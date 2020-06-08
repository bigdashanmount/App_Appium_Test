import time
#1、导入包
from appium import webdriver
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

#desired_caps["appPackage"] = 'com.boxuegu'
#desired_caps["appPackage"] = 'com.android.calculator2'
desired_caps["appPackage"] = 'com.android.settings'
#7、启动界面名appActivity
#desired_caps['appActivity'] = 'com.boxuegu.activity.MainFlutterActivity'
#desired_caps['appActivity'] = 'com.android.calculator2.Calculator'
desired_caps['appActivity'] = 'com.android.settings.Settings'
#8、http，连接appium服务器
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
#9、退出
time.sleep(5)
#获取数字1,id定位
#driver.find_element_by_id("com.android.calculator2:id/digit_1").click()
#获取数字1，name定位,已废弃
#driver.find_element_by_name("1").click()

#获取数字1，classname
#driver.find_element_by_class_name("android.widget.Button").click()
#button = driver.find_elements_by_class_name("android.widget.Button")
#print(button)
#button[1].click()

#获取数字1，xpath-文本定位
#xpath_text="//*[@text='1']"
#driver.find_element_by_xpath(xpath_text).click()
#driver.find_element_by_xpath("//*[@text='+']").click()
#driver.find_element_by_xpath("//*[@text='2']").click()
#driver.find_element_by_xpath("//*[@text='=']").click()
#xpath-id定位
#xpath_id="//*[@resource-id='com.android.calculator2:id/digit_1']"
#driver.find_element_by_xpath(xpath_id).click()
#xpath-class定位
#xpath_class_1 = '//android.widget.Button'
#xpath_class_2 = "//*[@class='android.widget.Button']"
#driver.find_elements_by_xpath(xpath_class_2)[6].click()

#xpath模糊定位contains text
#xpath_contains="//*[contains(@text,'屏幕锁定')]"
#driver.find_element_by_xpath(xpath_contains).click()
#xpath_contains_id = "//*[contains(@resource-id,'android:id/title')]"
#class @resource-id 换成class
#xpath_contains_list = driver.find_elements_by_xpath(xpath_contains_id)
#print(xpath_contains_list)


#starts-with
# xpath_starts = "//*[starts-with(@text,'网络')]"
# driver.find_element_by_xpath(xpath_starts).click()
# time.sleep(10)
time.sleep(3)
driver.close_app()
print(driver.current_package)
driver.quit()
