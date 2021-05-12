# 1.1 打开后台登录页面
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://127.0.0.1/admin.php")
# 1.2 输入用户名、密码、验证码
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("userpass").send_keys("password")
driver.find_element_by_name("userverify").send_keys("1234")
driver.find_element_by_css_selector('[type="submit"]').click()
# 2.1 在后台管理中心，点击商品管理
driver.find_element_by_link_text("商品管理").click()
# 2.2 点击添加商品
driver.find_element_by_xpath("/html/body/div[2]/ul[1]/li[2]/a").click()
# 2.3 输入商品名称
# 把selenium切换到子页面中
driver.switch_to.frame("mainFrame")
driver.find_element_by_xpath("/html/body/div[2]/div[2]/dl/form/dd[1]/ul/li[1]/input").send_keys(
    "iphone")
# 2.4 选择商品分类
driver.find_element_by_id("1").click()
driver.find_element_by_id("2").click()
driver.find_element_by_id("6").click()
# driver.find_element_by_id("7")
ActionChains(driver).double_click(driver.find_element_by_id("7")).perform()
# 2.5 选择商品品牌
brand = driver.find_element_by_name("brand_id")
Select(brand).select_by_value("1")
# 2.6 添加商品图片
driver.find_element_by_link_text("商品图册").click()
# #rt_rt_1el51uera1hk4h8179m53r5038 > label   css的元素定位
# #filePicker label
# driver.find_element_by_css_selector("#filePicker label").click()
driver.find_element_by_name("file").send_keys("D:/长颈鹿.jpg")
# 2.7 点击上传按钮
driver.find_element_by_css_selector(".uploadBtn.state-finish.state-ready").click()
# 2.8 处理弹出框
WebDriverWait(driver, 30, 0.5).until(expected_conditions.alert_is_present())
driver.switch_to.alert.accept()
# 2.9 点击提交按钮
driver.find_element_by_class_name("button_search").click()
