import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
# 智能等待之隐式等待
driver.implicitly_wait(10)
# 窗口最大化
driver.maximize_window()
# 1.登录
driver.get("http://127.0.0.1/index.php?m=user&c=public&a=login")
driver.find_element_by_id("username").send_keys("baishaojuan")
driver.find_element_by_id("password").send_keys("123321bai")
driver.find_element_by_class_name("login_btn").click()

# 2.点击进入“商城购物”
# 三种元素定位 id、classname、linkTest     导包快捷键 Alt + Enter
time.sleep(3)

driver.find_element_by_link_text("进入商城购物").click()

# 3.搜索iPhone
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/form/div/input[1]").send_keys("iphone")
driver.find_element_by_class_name("btn1").click()

# 4.点击商品图片
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[3]/div/div[1]/a/img").click()

# 5.切换窗口
# 5.1 找到新窗口的名字  -1保证找到最后一个窗口
new_window = driver.window_handles[-1]
# 5.2 切换到新窗口
driver.switch_to.window(new_window)

# 6.把选择的商品加入购物车
driver.find_element_by_id("joinCarButton").click()

# 7.去购物车结算
driver.find_element_by_class_name("shopCar_T_span3").click()
# 点击结算
# 第六种定位方法css selector
driver.find_element_by_css_selector(".shopCar_btn_03.fl").click()

# 8.添加新地址
driver.find_element_by_class_name("add-address").click()
# 9.输入收货人姓名
driver.find_element_by_name("address[address_name]").send_keys("小白")
# 10.输入手机号
driver.find_element_by_name("address[mobile]").send_keys("12345612345")
# 11.选择收货地区-省
sheng = driver.find_element_by_id("add-new-area-select")
Select(sheng).select_by_visible_text("山西省")
# 12.选择收货地区-市
shi = driver.find_elements_by_class_name("add-new-area-select")[1]
Select(shi).select_by_visible_text("大同市")
# 13.选择-地区
qu = driver.find_elements_by_tag_name("select")[2]
Select(qu).select_by_visible_text("市辖区")
# 14.地址
driver.find_element_by_name("address[address]").send_keys("莫须有小区")
driver.find_element_by_name("address[zipcode]").send_keys("00000")

driver.find_element_by_class_name("aui_state_highlight").click()




