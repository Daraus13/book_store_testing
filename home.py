##### Home: добавление комментария #####
import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
time.sleep(3)
driver.execute_script("window.scrollBy(0, 600);")
selenium_button = driver.find_element_by_class_name("wp-post-image").click()
reviews_button = driver.find_element_by_class_name("reviews_tab > a").click()
time.sleep(1)
star_button = driver.find_element_by_class_name("star-5").click()
time.sleep(1)
review = driver.find_element_by_id("comment")
review.send_keys("Nice book!")
time.sleep(1)
name = driver.find_element_by_id("author")
name.send_keys("Ivan")
time.sleep(1)
email = driver.find_element_by_id("email")
email.send_keys("Ivan_123@mail.ru")
time.sleep(1)
submit_button = driver.find_element_by_id("submit").click()
driver.quit()







