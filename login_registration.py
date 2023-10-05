##### Registration_login: регистрация аккаунта #####
# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# time.sleep(3)
# account_button = driver.find_element_by_css_selector("#menu-item-50 > a").click()
# email = driver.find_element_by_id("reg_email")
# email.send_keys("Ivan_123@mail.ru")
# time.sleep(1)
# password = driver.find_element_by_id("reg_password")
# password.send_keys("Ivan_123@009")
# time.sleep(1)
# register_button = driver.find_element_by_class_name("woocomerce-FormRow .button").click()
# driver.quit()


##### Registration_login: логин в систему #####
# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# time.sleep(3)
# account_button = driver.find_element_by_css_selector("#menu-item-50 > a").click()
# address= driver.find_element_by_id("username")
# address.send_keys("Ivan_123@mail.ru")
# time.sleep(1)
# password = driver.find_element_by_id("password")
# password.send_keys("Ivan_123@009")
# time.sleep(1)
# login_button = driver.find_element_by_class_name("form-row .button").click()
# time.sleep(1)
# logout_button = driver.find_element_by_class_name("woocommerce-MyAccount-navigation")
# logout_button_get_text = logout_button.text
# assert "Logout" in logout_button_get_text
# driver.quit()

