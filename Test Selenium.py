from selenium import webdriver

browser = webdriver.Edge(r'./.vscode/EdgeDriver.exe')
browser.get(r"https://www.baidu.com")
browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()
print(browser.page_source)