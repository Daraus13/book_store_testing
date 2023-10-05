##### Shop: отображение страницы товара #####
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# time.sleep(3)
# account_button = driver.find_element_by_css_selector("#menu-item-50 > a").click()
# address = driver.find_element_by_id("username")
# address.send_keys("Ivan_123@mail.ru")
# time.sleep(1)
# password = driver.find_element_by_id("password")
# password.send_keys("Ivan_123@009")
# time.sleep(1)
# shop_button = driver.find_element_by_css_selector("#menu-item-40 > a").click()
# time.sleep(1)
# html5 = driver.find_element_by_class_name("post-181 > a").click()
# some_element = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CLASS_NAME, "entry-summary"), "HTML5 Forms"))
# driver.quit()


##### Shop: отображение страницы товара #####
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# time.sleep(3)
# account_button = driver.find_element_by_css_selector("#menu-item-50 > a").click()
# address = driver.find_element_by_id("username")
# address.send_keys("Ivan_123@mail.ru")
# time.sleep(1)
# password = driver.find_element_by_id("password")
# password.send_keys("Ivan_123@009")
# time.sleep(1)
# shop_button = driver.find_element_by_css_selector("#menu-item-40 > a").click()
# time.sleep(1)
# html5 = driver.find_element_by_class_name("post-181 > a").click()
# some_element = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CLASS_NAME, "entry-summary"), "HTML5 Forms"))
# driver.quit()


##### Shop: количество товаров в категории #####
# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# time.sleep(3)
# account_button = driver.find_element_by_css_selector("#menu-item-50 > a").click()
# address = driver.find_element_by_id("username")
# address.send_keys("Ivan_123@mail.ru")
# time.sleep(1)
# password = driver.find_element_by_id("password")
# password.send_keys("Ivan_123@009")
# time.sleep(1)
# shop_button = driver.find_element_by_css_selector("#menu-item-40 > a").click()
# time.sleep(1)
# html_button = driver.find_element_by_class_name("cat-item-19 > a").click()
# time.sleep(1)
# items_count = driver.find_elements_by_class_name("type-product")
# if len(items_count) == 3:
#     print("Отображается 3 товара")
# else:
#     print("Ошибка. Количество товаров: " + str(len(items_count)))
# driver.quit()


##### Shop: сортировка товаров #####
# import time
# from selenium.webdriver.support.select import Select
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# time.sleep(3)
# account_button = driver.find_element_by_css_selector("#menu-item-50 > a").click()
# address = driver.find_element_by_id("username")
# address.send_keys("Ivan_123@mail.ru")
# time.sleep(1)
# password = driver.find_element_by_id("password")
# password.send_keys("Ivan_123@009")
# time.sleep(1)
# shop_button = driver.find_element_by_css_selector("#menu-item-40 > a").click()
# time.sleep(1)
# element = driver.find_element_by_class_name("orderby")
# select = Select(element)
# select.select_by_value("menu_order")
# sort = driver.find_element_by_css_selector("[value='price-desc']").click()
# element = driver.find_element_by_class_name("orderby")
# select = Select(element)
# select.select_by_value("price-desc")
# driver.quit()


##### Shop: отображение, скидка товара #####
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.get("https://practice.automationtesting.in/")
# driver.implicitly_wait(5)
# driver.maximize_window()
# account_button = driver.find_element_by_css_selector("#menu-item-50 > a").click()
# address = driver.find_element_by_id("username")
# address.send_keys("Ivan_123@mail.ru")
# password = driver.find_element_by_id("password")
# password.send_keys("Ivan_123@009")
# shop_button = driver.find_element_by_css_selector("#menu-item-40 > a").click()
# book_button = driver.find_element_by_class_name("attachment-shop_catalog").click()
# s_price = driver.find_element_by_class_name("woocommerce-Price-amount")
# s_price_get_text = s_price.text
# assert s_price_get_text == "₹600.00"
# n_price = driver.find_element_by_css_selector(".price > ins > span")
# n_price_get_text = n_price.text
# assert n_price_get_text == "₹450.00"
# book_cover = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, ".images")))
# book_cover.click()
# book_cover_close = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
# book_cover_close.click()
# driver.quit()


##### Shop: проверка цены в корзине #####
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.get("https://practice.automationtesting.in/")
# driver.implicitly_wait(5)
# driver.maximize_window()
# shop_button = driver.find_element_by_css_selector("#menu-item-40 > a").click()
# book_button = driver.find_element_by_css_selector(".post-182 > a:nth-child(2)").click()
# time.sleep(3)
# element = driver.find_element_by_class_name("cartcontents")
# element_get_text = element.text
# assert element_get_text == "1 Item"
# time.sleep(1)
# price = driver.find_element_by_class_name("amount")
# price_get_text = price.text
# assert price_get_text == "₹180.00"
# time.sleep(1)
# cor_button = driver.find_element_by_class_name("wpmenucart-contents").click()
# subtotal_element = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CLASS_NAME, "cart-subtotal .amount"), "180.00"))
# total_element = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CLASS_NAME, "order-total .amount"), "183.60"))
# driver.quit()


##### Shop: работа в корзине #####
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.get("https://practice.automationtesting.in/")
# driver.implicitly_wait(5)
# driver.maximize_window()
# shop_button = driver.find_element_by_css_selector("#menu-item-40 > a").click()
# driver.execute_script("window.scrollBy(0, 300);")
# book_button = driver.find_element_by_css_selector(".post-182 > a:nth-child(2)").click()
# time.sleep(1)
# boo_button = driver.find_element_by_css_selector(".post-180 > a:nth-child(2)").click()
# time.sleep(1)
# cor_button = driver.find_element_by_class_name("wpmenucart-contents").click()
# time.sleep(1)
# delete_button = driver.find_element_by_class_name("remove").click()
# time.sleep(1)
# undo_button = driver.find_element_by_link_text("Undo?").click()
# time.sleep(1)
# element = driver.find_element_by_class_name("input-text").clear()
# element1 = driver.find_element_by_class_name("input-text")
# element1.send_keys("3")
# time.sleep(1)
# update_button = driver.find_element_by_css_selector(".button:nth-child(2)").click()
# time.sleep(2)
# quant = driver.find_element_by_class_name("input-text")
# quant_select = quant.get_attribute("value")
# assert quant_select == "3"
# time.sleep(1)
# apply_button = driver.find_element_by_css_selector(".button:nth-child(3)").click()
# time.sleep(2)
# some_element = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-error"), "Please enter a coupon code."))
# driver.quit()


##### Shop: покупка товара #####
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.get("https://practice.automationtesting.in/")
# driver.implicitly_wait(5)
# driver.maximize_window()
# shop_button = driver.find_element_by_css_selector("#menu-item-40 > a").click()
# driver.execute_script("window.scrollBy(0, 300);")
# book_button = driver.find_element_by_css_selector(".post-182 > a:nth-child(2)").click()
# time.sleep(2)
# cor_button = driver.find_element_by_class_name("wpmenucart-contents").click()
# proceed_button = WebDriverWait(driver, 20).until(
#     EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button")) ).click()
# first_name = WebDriverWait(driver, 20).until(
#     EC.element_to_be_clickable((By.ID, "billing_first_name")) )
# first_name.send_keys("Ivan")
# last_name = driver.find_element_by_id("billing_last_name")
# last_name.send_keys("Petrov")
# email = driver.find_element_by_id("billing_email")
# email.send_keys("IvanP_13@mail.ru")
# phone = driver.find_element_by_id("billing_phone")
# phone.send_keys("89123456789")
# country = driver.find_element_by_class_name("select2-chosen").click()
# time.sleep(1)
# count = driver.find_element_by_id("s2id_autogen1_search")
# count.send_keys("Kenya")
# time.sleep(1)
# ck = driver.find_element_by_id("select2-results-1").click()
# time.sleep(1)
# address = driver.find_element_by_id("billing_address_1")
# address.send_keys("Gorodskaja 13")
# city = driver.find_element_by_id("billing_city")
# city.send_keys("Lamu")
# state = driver.find_element_by_id("billing_state")
# state.send_keys("Africa")
# pcode = driver.find_element_by_id("billing_postcode")
# pcode.send_keys("1234")
# driver.execute_script("window.scrollBy(0, 600);")
# time.sleep(3)
# check_pay = driver.find_element_by_css_selector("[value='cheque']")
# check_pay.click()
# place_button = driver.find_element_by_id("place_order").click()
# thank_element = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
# method_element = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CLASS_NAME, "method"), "Check Payments"))
# driver.quit()
