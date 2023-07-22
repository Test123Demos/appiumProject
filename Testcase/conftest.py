import pytest
from Testcase import app
from _pytest.nodes import Item
from _pytest.runner import CallInfo

'''进行appium包的配置'''
@pytest.fixture(scope="session")
def config_App():
    # 声明服务器地址
    server = 'http://localhost:4723/wd/hub'

    devices_system = {
        'automationName': 'appium',
        # 平台名
        'platformName': 'Android',
        # 设备名，可通过adb devices查询
        'driverName': '19111FDF600ADT',
        # 系统版本，可通过adb shell getprop ro.build.version.release，若是鸿蒙系统，写10.0
        'platformVersion': '13.0.0',
        # 浏览器名
        'browserName': 'chrome',
        # 浏览器驱动所在路径
        'chromedriverExecutable': 'D:/auto/app_auto/chromedriver.exe'
    }
    return server,devices_system

#自动执行app生成的对象
@pytest.fixture(scope="session",autouse=True)
def app_Init(config_App):
    server,devices_system=config_App
    app.Driver(server=server,devices_system=devices_system)
    app.imawait(5)