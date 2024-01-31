#from pyvirtualdisplay import Display
from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
#service = Service(executable_path='./chromedriver.exe')
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
# noinspection PyDeprecation
def send_proton_email(email_to, email_subject, email_message):
    driver = ''
    display = ''
    try:
        # display = Display(visible=0, size=(1920, 1080))   # Used to create a virtual display to be able to run selenium in a terminal without GUI
        # display.start()
        #driver = webdriver.Chrome(service=service)
        driver = webdriver.Firefox()
        driver.get('https://mail.protonmail.com/login')
        sleep(1)
        #driver.find_element_by_id('username').send_keys('Account_Username')
        driver.find_element(By.ID,'username').send_keys('Account_Username')
        #driver.find_element_by_id('password').send_keys('Account_password')
        driver.find_element(By.ID,'password').send_keys('Account_password')
        #driver.find_element_by_id('login_btn').click()
        driver.find_element(By.ID,'login_btn').click()
        sleep(3)
        #driver.find_element_by_id('password').send_keys('Mail_Decrypt_Password')
        driver.find_element(By.ID,'password').send_keys('Mail_Decrypt_Password')
        #driver.find_element_by_id('unlock_btn').click()
        driver.find_element(By.ID,'unlock_btn').click()
        sleep(5)
        #driver.find_element_by_xpath('//*[@id="pm_sidebar"]/section/a').click()
        driver.find_element(By.XPATH,'//*[@id="pm_sidebar"]/section/a').click()
        sleep(2)
        #driver.switch_to_active_element().send_keys(email_to + '\n' + '\t' + email_subject + '\t')
        driver.switch_to.active_element.send_keys(email_to + '\n' + '\t' + email_subject + '\t')
        sleep(0.5)
        driver.switch_to.active_element.send_keys(email_message + '\t' + '\t' + '\t' + '\t' + '\t' + '\t')
        sleep(0.5)
        driver.switch_to.active_element.click()
        sleep(5)
        driver.quit()
        # display.stop()
        print('E-mail Sent!')
        del email_subject
        del email_message
        del driver
        del display
    except Exception as err:
        driver.quit()
        # display.stop()
        print('\nError Occurred while sending e-mail!!')
        status = (str(err), 'Error Origin: Proton Mail Script')
        print(status)
        del err
        del status
        del driver
        # del display

testmsg = 'Thank you very much for your attention'
test = """Create a function get_largest_expression_result that accepts 2 numbers: a and b.
This function should compare the results of the following calculations and return the largest of them:
a + b
a - b
a * b
a / b
def get_largest_expression_result(a, b):
    if b==0:
        return f"Error: {b} must !=0"
    if (a+b)>=(a-b) and (a+b)>=a*b and (a+b)>=a/b:
        return a+b
    elif (a-b)>=(a+b) and (a-b)>=a*b and (a-b)>=a/b:
        return a-b
    elif a*b>=(a+b) and a*b>=(a-b) and a*b>=a/b:
        return a*b
    elif a/b>=(a+b) and a/b>=(a-b) and a/b>= a*b:
        return a/b
get_largest_expression_result(10, 5)
get_largest_expression_result(10, -5)
"""
send_proton_email('receiver_email@gmail.com', 'test', 'testmsg')
