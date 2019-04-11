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


# 登录
def login(list, n = 1):  # list:数据     n:循环次数
    if len(list) == 0:
        print "数据为空"
        exit(2)
    for i in range(n):
        s = list[i]
        username = str((s[u'userName']))
        password = str((s[u'password']))
        if username.isspace() or password.isspace() or len(username) == 0 or len(password) == 0:  # 判断输入的用户名或密码是否为空
            print('用户名或密码不能为空')
            exit(3)

        driver.find_element_by_xpath(
            "/html/body/div[1]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[1]").click()
        driver.find_element_by_name("userName").clear()
        driver.find_element_by_name("userName").send_keys(username)
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys(password)
        driver.find_element_by_name("login").click()
        if i < n - 1:
            driver.back()


# 注册
def register(list, n = 1):  # list:数据     n:循环次数
    if len(list) == 0:
        print "数据为空"
        exit(2)
    for i in range(n):
        s = list[i]
        driver.find_element_by_xpath(
            "/html/body/div[1]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[2]").click()  # 注册

        if str(s[u'userName']).isspace() or str(s[u'password']).isspace() or len(str(s[u'userName'])) == 0 or len(str(s[u'password'])) == 0:  # 判断输入的用户名或密码是否为空
            print('用户名或密码不能为空')
            exit(3)
        driver.find_element_by_name("firstName").clear()
        driver.find_element_by_name("firstName").send_keys(str(s[u'firstName']))
        time.sleep(0.2)
        driver.find_element_by_name("lastName").clear()
        driver.find_element_by_name("lastName").send_keys(str(s[u'lastName']))
        time.sleep(0.2)
        driver.find_element_by_name("phone").clear()
        driver.find_element_by_name("phone").send_keys(str(int(s[u'phone'])))
        time.sleep(0.2)
        driver.find_element_by_name("userName").clear()
        driver.find_element_by_name("userName").send_keys(str(s[u'userName']))
        time.sleep(0.2)
        driver.find_element_by_name("address1").clear()
        driver.find_element_by_name("address1").send_keys(str(s[u'address1']))
        time.sleep(0.2)
        driver.find_element_by_name("address2").clear()
        driver.find_element_by_name("address2").send_keys(str(s[u'address2']))
        time.sleep(0.2)
        driver.find_element_by_name("city").clear()
        driver.find_element_by_name("city").send_keys(str(s[u'city']))
        time.sleep(0.2)
        driver.find_element_by_name("state").clear()
        driver.find_element_by_name("state").send_keys(str(s[u'state']))
        time.sleep(0.2)
        driver.find_element_by_name("postalCode").clear()
        driver.find_element_by_name("postalCode").send_keys(str(int(s[u'postalCode'])))
        time.sleep(0.2)

        s1 = Select(driver.find_element_by_name("country"))
        # s1.select_by_index(1)  # 选择第几项
        # s1.select_by_value("38")  # 选择value="?"的项
        s1.select_by_visible_text(str(s[u'country']))  # 选择text="?"的值
        time.sleep(0.2)

        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys(str(s[u'email']))
        time.sleep(0.2)
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys(str(s[u'password']))
        time.sleep(0.2)
        driver.find_element_by_name("confirmPassword").clear()
        driver.find_element_by_name("confirmPassword").send_keys(str(s[u'confirmPassword']))
        time.sleep(0.2)
        if str(s[u'password']).equals(str(s[u'confirmPassword'])) == False:  # 判断输入密码是否相同
            print('输入密码不相同')
            exit(4)

        driver.find_element_by_name("register").click()
        time.sleep(0.2)
        if i < n - 1:
            driver.back()


def putin(list, n = 1):  # list:数据     n:循环次数
    if len(list) == 0:
        print "数据为空"
        exit(2)
    for i in range(n):
        s = list[i]
        tourtype = int(s[u'tourtype'])
        if tourtype == 1:
            driver.find_element_by_xpath('//input[@value="roundtrip"]').click()
        else:
            driver.find_element_by_xpath('//input[@value="oneway"]').click()
        time.sleep(0.1)

        s1 = Select(driver.find_element_by_name("passCount"))
        s1.select_by_visible_text("1")
        time.sleep(0.1)

        s2 = Select(driver.find_element_by_name("fromPort"))
        s2.select_by_index(str(int(s[u'fromPort'])))
        time.sleep(0.1)

        s3 = Select(driver.find_element_by_name("fromMonth"))
        s3.select_by_index(str(int(s[u'fromMonth'])))  # April
        time.sleep(0.1)

        s4 = Select(driver.find_element_by_name("fromDay"))
        s4.select_by_index(str(int(s[u'fromDay'])))
        time.sleep(0.1)

        s5 = Select(driver.find_element_by_name("toPort"))
        s5.select_by_index(str(int(s[u'toPort'])))
        time.sleep(0.1)

        s6 = Select(driver.find_element_by_name("toMonth"))
        s6.select_by_index(str(int(s[u'toMonth'])))  # May
        time.sleep(0.1)

        s7 = Select(driver.find_element_by_name("toDay"))
        s7.select_by_index(str(int(s[u'toDay'])))
        time.sleep(0.1)

        seatclass = int(s[u'seatclass'])
        if seatclass == 1:
            driver.find_element_by_xpath('//input[@value="Coach"]').click()
        if seatclass == 2:
            driver.find_element_by_xpath('//input[@value="Business"]').click()
        if seatclass == 3:
            driver.find_element_by_xpath('//input[@value="First"]').click()

        time.sleep(0.1)

        s8 = Select(driver.find_element_by_name("airline"))
        s8.select_by_index(str(int(s[u'airline'])))
        time.sleep(0.1)

        driver.find_element_by_name("findFlights").click()
        if i < n - 1:
            driver.back()


def selectFlights(list, n = 1):  # list:数据     n:循环次数
    if len(list) == 0:
        print "数据为空"
        exit(2)
    for i in range(n):
        s = list[i]
        DEPART = int(s[u'DEPART'])
        if DEPART == 1:
            driver.find_element_by_xpath(
                '/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table[1]/tbody/tr[3]/td[1]/input').click()
        if DEPART == 2:
            driver.find_element_by_xpath(
                '/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table[1]/tbody/tr[5]/td[1]/input').click()
        if DEPART == 3:
            driver.find_element_by_xpath(
                '/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table[1]/tbody/tr[7]/td[1]/input').click()
        if DEPART == 4:
            driver.find_element_by_xpath(
                '/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table[1]/tbody/tr[9]/td[1]/input').click()

        RETURN = int(s[u'RETURN'])
        if RETURN == 1:
            driver.find_element_by_xpath(
                '/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table[2]/tbody/tr[3]/td[1]/input').click()
        if RETURN == 2:
            driver.find_element_by_xpath(
                '/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table[2]/tbody/tr[5]/td[1]/input').click()
        if RETURN == 3:
            driver.find_element_by_xpath(
                '/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table[2]/tbody/tr[7]/td[1]/input').click()
        if RETURN == 4:
            driver.find_element_by_xpath(
                '/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table[2]/tbody/tr[9]/td[1]/input').click()
        time.sleep(0.5)
        driver.find_element_by_name("reserveFlights").click()
        if i < n - 1:
            driver.back()


def buyFlights(list, n = 1):  # list:数据     n:循环次数
    if len(list) == 0:
        print "数据为空"
        exit(2)
    for i in range(n):
        s = list[i]
        driver.find_element_by_name("passFirst0").clear()
        driver.find_element_by_name("passFirst0").send_keys(str(s[u'passFirst0']))
        driver.find_element_by_name("passLast0").clear()
        driver.find_element_by_name("passLast0").send_keys(str(s[u'passLast0']))
        s8 = Select(driver.find_element_by_name("pass.0.meal"))
        s8.select_by_index(str(int(s[u'pass.0.meal'])))
        time.sleep(0.1)

        s9 = Select(driver.find_element_by_name("creditCard"))
        s9.select_by_index(str(int(s[u'creditCard'])))
        driver.find_element_by_name("creditnumber").clear()
        driver.find_element_by_name("creditnumber").send_keys(str(int(s[u'creditnumber'])))
        s10 = Select(driver.find_element_by_name("cc_exp_dt_mn"))
        s10.select_by_index(str(int(s[u'cc_exp_dt_mn'])))
        s11 = Select(driver.find_element_by_name("cc_exp_dt_yr"))
        s11.select_by_index(str(int(s[u'cc_exp_dt_yr'])))
        time.sleep(0.1)

        driver.find_element_by_name("cc_frst_name").clear()
        driver.find_element_by_name("cc_frst_name").send_keys(str(s[u'cc_frst_name']))
        driver.find_element_by_name("cc_mid_name").clear()
        driver.find_element_by_name("cc_mid_name").send_keys(str(s[u'cc_mid_name']))
        driver.find_element_by_name("cc_last_name").clear()
        driver.find_element_by_name("cc_last_name").send_keys(str(s[u'cc_last_name']))
        time.sleep(0.1)

        if int(s[u'ticketless']) == 1:
            driver.find_element_by_xpath(
                "/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[9]/td[2]/input").click()
        driver.find_element_by_name("billAddress1").clear()
        driver.find_element_by_name("billAddress1").send_keys(str(s[u'billAddress1']))
        driver.find_element_by_name("billAddress2").clear()
        driver.find_element_by_name("billAddress2").send_keys(str(s[u'billAddress2']))
        driver.find_element_by_name("billCity").clear()
        driver.find_element_by_name("billCity").send_keys(str(s[u'billCity']))
        driver.find_element_by_name("billState").clear()
        driver.find_element_by_name("billState").send_keys(str(s[u'billState']))
        driver.find_element_by_name("billZip").clear()
        driver.find_element_by_name("billZip").send_keys(str(int(s[u'billZip'])))
        s12 = Select(driver.find_element_by_name("billCountry"))
        s12.select_by_visible_text(str(s[u'billCountry']))
        time.sleep(0.1)

        if int(s[u'sameasbill']) == 1:
            driver.find_element_by_xpath(
                "/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[15]/td[2]/input").click()
        driver.find_element_by_name("delAddress1").clear()
        driver.find_element_by_name("delAddress1").send_keys(str(s[u'delAddress1']))
        driver.find_element_by_name("delAddress2").clear()
        driver.find_element_by_name("delAddress2").send_keys(str(s[u'delAddress2']))
        driver.find_element_by_name("delCity").clear()
        driver.find_element_by_name("delCity").send_keys(str(s[u'delCity']))
        driver.find_element_by_name("delState").clear()
        driver.find_element_by_name("delState").send_keys(str(s[u'delState']))
        driver.find_element_by_name("delZip").clear()
        driver.find_element_by_name("delZip").send_keys(str(int(s[u'delZip'])))
        s13 = Select(driver.find_element_by_name("delCountry"))
        s13.select_by_visible_text(str(s[u'delCountry']))
        time.sleep(0.1)

        driver.find_element_by_name("buyFlights").click()
        if i < n - 1:
            driver.back()


if __name__ == '__main__':

    driver = webdriver.Chrome()
    driver.get('http://newtours.demoaut.com/')
    print driver.current_url
    print driver.title
    try:
        assert driver.current_url.__contains__("http://newtours.demoaut.com/")
    except:
        print "expected_url:" + "http://newtours.demoaut.com/"
        print "未跳转到正确页面\n"
        exit(1)

    # 登录
    list = excel_table_byindex("test.xls", 0, 0)
    login(list, 1)
    print driver.current_url
    print driver.title
    try:
        assert driver.current_url.__contains__("http://newtours.demoaut.com/mercuryreservation.php")
    except:
        print "expected_url:" + "http://newtours.demoaut.com/mercuryreservation.php"
        print "未跳转到正确页面\n"
        exit(1)

    # 填写信息
    time.sleep(1)
    list = excel_table_byindex("test.xls", 0, 2)
    putin(list, 1)
    print driver.current_url
    print driver.title
    try:
        assert driver.current_url.__contains__("http://newtours.demoaut.com/mercuryreservation2.php")
    except:
        print "expected_url:" + "http://newtours.demoaut.com/mercuryreservation2.php"
        print "未跳转到正确页面\n"
        exit(1)

    # 选择航班
    list = excel_table_byindex("test.xls", 0, 3)
    selectFlights(list, 1)
    print driver.current_url
    print driver.title
    try:
        assert driver.current_url.__contains__("http://newtours.demoaut.com/mercurypurchase.php")
    except:
        print "expected_url:" + "http://newtours.demoaut.com/mercurypurchase.php"
        print "未跳转到正确页面\n"
        exit(1)
    time.sleep(2)

    # 购买机票
    list = excel_table_byindex("test.xls", 0, 4)
    buyFlights(list, 1)
    print driver.current_url
    print driver.title
    try:
        assert driver.current_url.__contains__("http://newtours.demoaut.com/mercurypurchase2.php")
    except :
        print "expected_url:" + "http://newtours.demoaut.com/mercurypurchase2.php"
        print "未跳转到正确页面\n"
        exit(1)

    # driver.quit()
