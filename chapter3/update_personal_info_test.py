import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
# 1.登录
driver.get("http://127.0.0.1/index.php?m=user&c=public&a=login")
driver.find_element_by_id("username").send_keys("baishaojuan")
driver.find_element_by_id("password").send_keys("123321bai")
#driver.find_element_by_class_name("login_btn").click()
# submit方法，类似于click，只能用于form表单中
# 这里submit方法就代替了，定位登录按钮并点击的操作
driver.find_element_by_id("password").submit()

#批量注释的快捷键：Ctrl + /
# 2.1 点击账号设置
driver.find_element_by_link_text("账号设置").click()
# # 2.2 点击个人资料    可以只写人资，取部分文本
driver.find_element_by_partial_link_text("个人资料").click()
# 2.3 修改真实姓名
driver.find_element_by_id("true_name").clear()
driver.find_element_by_id("true_name").send_keys("小白")
# 2.4 选择性别   有两对双引号时，需要把其中一对改成单引号
driver.find_element_by_css_selector('[value="2"]').click()
#driver.find_element_by_css_selector("[value='2']").click()
# 2.5 输入生日
# 2.5.1 删除readonly属性
scprit = 'document.getElementById("date").removeAttribute("readonly")'
driver.execute_script(scprit)
# 2.5.2 在生日输入框中输入新的生日
driver.find_element_by_id("date").clear()
driver.find_element_by_id("date").send_keys("1990-09-09")
# 2.6 输入QQ
driver.find_element_by_id("qq").clear()
driver.find_element_by_id("qq").send_keys("1234567890")
# 2.7 点击确定
driver.find_element_by_css_selector('[value="确认"]').click()
# 弹出框的确定按钮
time.sleep(3)
WebDriverWait(driver,30,0.5).until(expected_conditions.alert_is_present())
undate_status = driver.switch_to.alert.text
print(undate_status)
driver.switch_to.alert.accept()
