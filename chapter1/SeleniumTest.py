from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.find_element_by_id("kw").send_keys("软件测试")
driver.find_element_by_id("su").click()