import time  # Nhập module time để sử dụng hàm sleep

import undetected_chromedriver as uc
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.remote.webdriver import By
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

options = uc.ChromeOptions()
options.add_argument("--window-size=600,300")

driver = uc.Chrome(options=options)
driver.get("https://www.tiktok.com/signup/phone-or-email/email")
time.sleep(5)  # Đợi 20 giây

# WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginContainer"]/div/div/div/div[2]/div[2]/div[2]/div/div'))).click()
#By.CSS_SELECTOR, By.XPATH, By.ID, By.TAG_NAME
#.find_element, .find_elements()[0], .send_keys(), .click(), .click_safe()
# driver.find_element(By.CSS_SELECTOR, "h1[class='hero-headline no-title no-toc no-anchor']")[0]


WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginContainer"]/div[1]/form/div[2]/div[1]'))).click_safe()

WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, '//input[@name="email"]'))).send_keys("an394@gmail.com")
WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, '//input[@type="password"]'))).send_keys("123456789")

time.sleep(10)  # Đợi 20 giây

driver.quit()
time.sleep(10)  # Tăng thời gian chờ lên 10 giây
print("Xong")
