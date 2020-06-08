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
time.sleep(5)
driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()



#计算原坐标点
#获取终止坐标Y轴-起始坐标Y，得到中心的值/2
#起始坐标Y+ 除以2的值 ，滑动Y轴坐标
#1046-504 = 500/2 = 250
#504+250 = 750    Y轴
#   700 x轴


#拖动终止坐标
#Y轴
#获取手机的宽和高，高度*3/4
#driver可以获取
screen = driver.get_window_size()
#print(screen)
#screen*3/4
time.sleep(5)
driver.swipe(700,750,700,screen["height"]*3/4,3000)
time.sleep(5)
#相对定位，获取手机的宽和高，* 相应比例
#向上X轴不变，y轴变化
#driver.swipe(screen["width"]*0.5,screen["height"]*3/4,screen["width"]*0.5,screen["height"]*1/4,3000)
#time.sleep(5)
#向下X轴不变，y轴变化
#driver.swipe(screen["width"]*0.5,screen["height"]*1/4,screen["width"]*0.5,screen["height"]*3/4,3000)

#向右Y轴不变，x轴变化
driver.swipe(screen["width"]*0.75,screen["height"]*0.5,screen["width"]*0.2,screen["height"]*0.5,3000)
#向左Y轴不变，x轴变化
time.sleep(5)
#driver.swipe(screen["width"]*0.2,screen["height"]*0.5,screen["width"]*0.75,screen["height"]*0.5,3000)

#driver.save_screenshot("滑动截图.png")
driver.get_screenshot_as_file('screenshot/滑动截图文件.png')
# driver.swipe()
time.sleep(10)
driver.quit()
