# coding=utf-8
from selenium.webdriver import Firefox
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
import xlrd
import time
from selenium.webdriver.support.ui import WebDriverWait

class MyListener(AbstractEventListener):
    def before_navigate_to(self, url, driver):
        print("Before navigate to %s" % url)
    def after_navigate_to(self, url, driver):
        print("After navigate to %s" % url)


driver = Firefox()
wait = WebDriverWait(driver, 2)
ef_driver=EventFiringWebDriver(driver,MyListener())
ef_driver.get("http://www.sf-express.com/cn/sc/dynamic_function/waybill/#search/bill-number/")

# 读取订单号
data = xlrd.open_workbook('shunfeng.xlsx')
table = data.sheets()[0]
nrows = table.nrows
dingdan = ''
for i in range(nrows ):
    dingdan += (table.row_values(i)[0]).strip(' ') + "\t"
    print(table.row_values(i)[0].strip(''))
print(dingdan)

time.sleep(2)
# 打开网页，先加载资源，如果网络不好的可以把上面的2换大点
ef_driver.find_element_by_class_name("token-input").send_keys(dingdan)
time.sleep(0.3)
# 程序从excel读取订单号粘贴进来
driver.find_element_by_id("queryBill").click()
time.sleep(8)
# 8秒的时间来输入验证码，如果太短可以把8换大点

# 打开所有的栏目
openlist = driver.find_elements_by_class_name("open")
for i in range(len(openlist)):
    openlist[i].click()
    time.sleep(0.2)
time.sleep(1)

alllidt = driver.find_elements_by_class_name("status-update-box")
for i in range(len(alllidt)):
    alllidt[i].click()
    time.sleep(0.2)
time.sleep(2)
# 打开所有的栏目end

filename = 'output.txt'
# 遍历所有的结果然后输出
deliveryList = driver.find_elements_by_class_name("delivery")
for i in range(len(deliveryList)):
    print("\n订单号：" + deliveryList[i].find_elements_by_class_name("number")[0].text)
    with open(filename, 'a') as fileobject:  # 使用‘a’来提醒python用附加模式的方式打开
        fileobject.write("\n\n订单号：" + deliveryList[i].find_elements_by_class_name("number")[0].text)
    datelist = deliveryList[i].find_elements_by_class_name("route")
    for j in range(len(datelist)):
        print("\n状态："+datelist[j].find_elements_by_class_name('route-status-text')[0].find_elements_by_xpath('span')[0].text)
        print("\n时间："+datelist[j].find_elements_by_class_name('route-date-time')[0].find_elements_by_xpath('span')[0].text)
        print("\n详情："+datelist[j].find_elements_by_class_name('route-desc')[0].find_elements_by_xpath('span')[0].text)
        with open(filename, 'a') as fileobject:  # 使用‘a’来提醒python用附加模式的方式打开
            fileobject.write("\n  "+datelist[j].find_elements_by_class_name('route-status-text')[0].find_elements_by_xpath('span')[0].text)
        with open(filename, 'a') as fileobject:  # 使用‘a’来提醒python用附加模式的方式打开 
            fileobject.write("  "+datelist[j].find_elements_by_class_name('route-date-time')[0].find_elements_by_xpath('span')[0].text)
        with open(filename, 'a') as fileobject:  # 使用‘a’来提醒python用附加模式的方式打开
            fileobject.write("  "+datelist[j].find_elements_by_class_name('route-desc')[0].find_elements_by_xpath('span')[0].text)



# 关闭浏览器
# ef_driver.close()