#====================================#
##КНИГА ОТ СОЗДАТЕЛЯ ГУГЛА ПРО ВЭБ####
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from time import sleep
# def check_tipcalculator():
#     driver = webdriver.Chrome(executable_path="C:\\Program Files (x86)\\chromedriver.exe")
#     driver.get('file:///D:/DEvOPs/Class%204/tip_calc/index.html')
#     driver.find_element_by_id('billamt').send_keys('100')
#     driver.find_element_by_id('peopleamt').send_keys('5')
#     driver.find_element_by_xpath('//*[@id="serviceQual"]/option[3]').click()
#     driver.find_element_by_id('musicamt').send_keys('5')
#     driver.find_element_by_id('calculate').click()
#     #sleep(5)
#     # # driver.refresh()
#     # # sleep(5)
#     # # #print(driver.current_url)
#     # # #print(driver.title)
#     # # #print(driver.page_source)
#     driver.close()
# for i in range(5):
#     check_tipcalculator()
#     sleep(5)

#===========================[the same with func and try(doesn't work]====

# from selenium import webdriver
# from time import sleep
# driver = webdriver.Chrome(executable_path="C:\\Program Files (x86)\\chromedriver.exe")
# driver.get('file:///D:/DEvOPs/Class%204/tip_calc/index.html')
#
# def find_by_id(driver,elem_id):
#     try:
#         return driver.find_element_by_id(elem_id)
#     except TypeError as e:
#         return None
#
# def check_tipcalculator(driver):
#     bill = find_by_id(driver, 'billamt')
#     bill.send_keys('100')
#     #find_by_id(driver, '5')
#     #driver.find_element_by_xpath('//*[@id="serviceQual"]/option[3]').click()
#     #find_by_id(driver, '5')
#     #find_by_id('calculate').click()
#
#
# for i in range(5):
#     check_tipcalculator(driver)
#     sleep(5)

#=================== RETURN DATA FROM  WEB PAGE FIELD=======================
driver = webdriver.Chrome(executable_path="C:\\Program Files (x86)\\chromedriver.exe")
# driver.get('file:///D:/DEvOPs/Class%204/tip_calc/index.html')
#
# def run_test(driver_to_user):
#     driver.find_element_by_id('billamt').send_keys('100')
#     driver.find_element_by_id('peopleamt').send_keys('5')
#     driver.find_element_by_xpath('//*[@id="serviceQual"]/option[3]').click()
#     driver.find_element_by_id('musicamt').send_keys('5')
#     driver.find_element_by_id('calculate').click()
#     a = driver.find_element_by_id('tip').text
#     if a.text == 5.00:
#         return  0
#
# b = run_test(driver)
# if b == 0:
#     print("Very Good")
#============================= [[ HOT KEYS ]DOESn't WORK!!]=================
driver.get('file:///D:/DEvOPs/Class%204/tip_calc/index.html')
driver.find_element_by_id('billamt').send_keys('100'+Keys.TAB + Keys.DOWN*3+'5'+Keys.TAB)


#==============================[[ CONDITIONAL SYNCHRONIZATION]]============
driver.implicitly_wait(4)

