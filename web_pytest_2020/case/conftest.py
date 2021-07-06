from selenium import webdriver
import time
import pytest
from pages.login_page import LoginPage
from selenium.webdriver.chrome.options import Options
import os
import platform

@pytest.fixture(scope="session")
def driver(request):

    # linux
    if platform.system() == "windows":
        _driver = webdriver.Chrome()
        _driver.maximize_window()  # 最大化
    else:
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # 无界面
        chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在报错问题
        chrome_options.add_argument('--disable-gpu')  # 禁用GPU硬件加速。如果软件渲染器没有就位，则GPU进程将不会启动
        chrome_options.add_argument('--disable-dev-shm-usage')

        # windows
        '''定义全局driver'''
        #_driver = webdriver.Chrome()
        _driver = webdriver.Chrome(chrome_options=chrome_options)
        #_driver.maximize_window()  # 最大化

    def end():
        '''测试用例完成后，执行终结函数'''
        time.sleep(5)
        _driver.quit()

    request.addfinalizer(end)
    return _driver



@pytest.fixture(scope="session")
def login(driver):
    '''前置：登录'''
    web = LoginPage(driver)
    web.login()
    return driver


