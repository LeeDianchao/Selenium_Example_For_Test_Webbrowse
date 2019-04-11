#-*-coding:utf-8-*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import xlrd


def open_excel(file = 'test.xls'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception, e:
        print str(e)


# 根据索引获取Excel表格中的数据 参数:file：Excel文件路径 colnameindex：表头列名所在行的索引 ，by_index：表的索引
def excel_table_byindex(file= 'test.xls', colnameindex=0, by_index=0):
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows  # 行数
    colnames = table.row_values(colnameindex)  # 某一行数据
    list = []
    for rownum in range(1, nrows):
        row = table.row_values(rownum)
        if row:
            app = {}
            for i in range(len(colnames)):
                app[colnames[i]] = row[i]
            list.append(app)
    return list


list = excel_table_byindex("test.xls", 0, 1)
print list

driver = webdriver.Chrome()
driver.get('http://newtours.demoaut.com')
print driver.current_url
print driver.title
# assert driver.current_url.__eq__("https://www.baidu.com/")

# 登录
def login():
    driver.find_element_by_xpath(
        "/html/body/div[1]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[1]").click()
    driver.find_element_by_name("userName").send_keys("123")
    driver.find_element_by_name("password").send_keys("123")
    driver.find_element_by_name("login").click()


# driver.find_element_by_xpath("/html/body/div[1]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[2]/td[2]").send_keys("123")
# 注册
def register():
    driver.find_element_by_xpath(
        "/html/body/div[1]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[2]").click()  # 注册
    driver.find_element_by_name("firstName").send_keys("123")
    time.sleep(0.2)
    driver.find_element_by_name("lastName").send_keys("123")
    time.sleep(0.2)
    driver.find_element_by_name("phone").send_keys("123")
    time.sleep(0.2)
    driver.find_element_by_name("userName").send_keys("123")
    time.sleep(0.2)
    driver.find_element_by_name("address1").send_keys("123")
    time.sleep(0.2)
    driver.find_element_by_name("address2").send_keys("123")
    time.sleep(0.2)
    driver.find_element_by_name("city").send_keys("123")
    time.sleep(0.2)
    driver.find_element_by_name("state").send_keys("123")
    time.sleep(0.2)
    driver.find_element_by_name("postalCode").send_keys("123")
    time.sleep(0.2)

    s1 = Select(driver.find_element_by_name("country"))
    # s1.select_by_index(1)  # 选择第几项
    # s1.select_by_value("38")  # 选择value="?"的项
    s1.select_by_visible_text("CHINA")  # 选择text="o3"的值

    time.sleep(0.2)
    driver.find_element_by_name("email").send_keys("123")
    time.sleep(0.2)
    driver.find_element_by_name("password").send_keys("123")
    time.sleep(0.2)
    driver.find_element_by_name("confirmPassword").send_keys("123")
    time.sleep(0.2)

    driver.find_element_by_name("register").click()
    time.sleep(0.2)


def putin():
    driver.find_element_by_xpath('//input[@value="oneway"]').click()
    time.sleep(0.1)

    s1 = Select(driver.find_element_by_name("passCount"))
    s1.select_by_index("1")
    time.sleep(0.1)

    s2 = Select(driver.find_element_by_name("fromPort"))
    s2.select_by_index("5")
    time.sleep(0.1)

    s3 = Select(driver.find_element_by_name("fromMonth"))
    s3.select_by_index("4")  # April
    time.sleep(0.1)

    s4 = Select(driver.find_element_by_name("fromDay"))
    s4.select_by_index("20")
    time.sleep(0.1)

    s5 = Select(driver.find_element_by_name("toPort"))
    s5.select_by_index("3")
    time.sleep(0.1)

    s6 = Select(driver.find_element_by_name("toMonth"))
    s6.select_by_index("5")  # May
    time.sleep(0.1)

    s7 = Select(driver.find_element_by_name("toDay"))
    s7.select_by_index("21")
    time.sleep(0.1)

    driver.find_element_by_xpath('//input[@value="First"]').click()
    time.sleep(0.1)

    s8 = Select(driver.find_element_by_name("airline"))
    s8.select_by_index("2")
    time.sleep(0.1)

    driver.find_element_by_name("findFlights").click()

    driver.find_element_by_xpath('/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table[1]/tbody/tr[3]/td[1]/input').click()
    # driver.find_element_by_xpath('/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table[1]/tbody/tr[5]/td[1]/input').click()
    # driver.find_element_by_xpath('/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table[1]/tbody/tr[7]/td[1]/input').click()
    # driver.find_element_by_xpath('/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table[1]/tbody/tr[9]/td[1]/input').click()
    #
    # driver.find_element_by_xpath('/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table[2]/tbody/tr[3]/td[1]/input').click()
    # driver.find_element_by_xpath('/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table[2]/tbody/tr[5]/td[1]/input').click()
    # driver.find_element_by_xpath('/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table[2]/tbody/tr[7]/td[1]/input').click()
    driver.find_element_by_xpath('/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table[2]/tbody/tr[9]/td[1]/input').click()

    driver.find_element_by_name("reserveFlights").click()

    driver.find_element_by_name("passFirst0").send_keys("22")
    time.sleep(0.1)
    driver.find_element_by_name("passLast0").send_keys("22")
    time.sleep(0.1)
    s8 = Select(driver.find_element_by_name("pass.0.meal"))
    s8.select_by_index("2")
    time.sleep(0.1)

    s9 = Select(driver.find_element_by_name("creditCard"))
    s9.select_by_index("2")
    time.sleep(0.1)
    driver.find_element_by_name("creditnumber").send_keys("123")
    time.sleep(0.1)
    s10 = Select(driver.find_element_by_name("cc_exp_dt_mn"))
    s10.select_by_index("2")
    time.sleep(0.1)
    s11 = Select(driver.find_element_by_name("cc_exp_dt_yr"))
    s11.select_by_index("2")
    time.sleep(0.1)

    driver.find_element_by_name("cc_frst_name").send_keys("sd")
    driver.find_element_by_name("cc_mid_name").send_keys("ab")
    driver.find_element_by_name("cc_last_name").send_keys("acv")
    time.sleep(0.1)

    driver.find_element_by_xpath(
        "/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[9]/td[2]/input").click()
    time.sleep(0.1)
    driver.find_element_by_name("billAddress1").send_keys("ba1")
    driver.find_element_by_name("billAddress2").send_keys("ba2")
    driver.find_element_by_name("billCity").send_keys("bc")
    driver.find_element_by_name("billState").send_keys("bs")
    driver.find_element_by_name("billZip").send_keys("bz")
    time.sleep(0.1)
    s7 = Select(driver.find_element_by_name("billCountry"))
    s7.select_by_index("1")
    time.sleep(0.1)

    driver.find_element_by_xpath(
        "/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[15]/td[2]/input").click()
    driver.find_element_by_name("delAddress1").send_keys("da1")
    driver.find_element_by_name("delAddress2").send_keys("da2")
    driver.find_element_by_name("delCity").send_keys("dc")
    driver.find_element_by_name("delState").send_keys("ds")
    driver.find_element_by_name("delZip").send_keys("dz")
    time.sleep(0.1)
    s7 = Select(driver.find_element_by_name("delCountry"))
    s7.select_by_index("1")
    time.sleep(0.1)

    driver.find_element_by_name("buyFlights")


login()
time.sleep(1)
putin()

# driver.quit()
