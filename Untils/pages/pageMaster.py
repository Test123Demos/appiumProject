from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


class App():
    def Driver(self,server:str,devices_system:dict):
        self.driver = webdriver.Remote(server, devices_system)

    def imawait(self,time):
        self.driver.implicitly_wait(time)
    def element(self,parms:tuple):
        types,value=parms
        e=None
        if types.lower()=="id":
            e=self.driver.find_element(AppiumBy.ID,"{}".format(value))
        elif types.lower()=="xpath":
            e=self.driver.find_element(AppiumBy.XPATH,f"{value}")
        elif types.lower()=="text":
            e=self.driver.find_element(AppiumBy.LINK_TEXT,f"{value}")
        if e is not None:
            return e
        else:
            raise Exception("传入的定位方式类型有问题！")

    def esendText(self,parms:tuple,value:str): #定位到元素并输入
        self.element(parms).send_keys(f"{value}")

    def sendText(self,e,value:str):
        e.send_keys(f"{value}")

    def eclick(self,parms:tuple):#定位并点击
        self.element(parms).click()

    def click(self,e):
        e.click()


