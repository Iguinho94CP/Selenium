from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import urllib
import time

"""
A simple script made using SELENIUM to extract the URL from a given number of images
"""

driver = webdriver.Chrome()
driver.get('https://www.google.com.br/search?q=dogs&hl=en&authuser=0&tbm=isch&sxsrf=ALiCzsZBseAj37iW9CxrrAbUsc3t10af6A%3A1657654930232&source=hp&biw=1920&bih=942&ei=ks7NYqfcC-295OUPg66J6AI&iflsig=AJiK0e8AAAAAYs3copW7FHarQ_hy7JAuGxgxkVIjaJsf&ved=0ahUKEwin7ZjqjfT4AhXtHrkGHQNXAi0Q4dUDCAc&uact=5&oq=dogs&gs_lcp=CgNpbWcQAzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgARQAFiZCWDrFmgAcAB4AIABtgGIAZEFkgEDMC40mAEAoAEBqgELZ3dzLXdpei1pbWc&sclient=img')

driver.find_element(By.XPATH, '//*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img').click()
time.sleep(2)
count = 0
while count <= 5:
    next_arrow = driver.find_element(By.XPATH, '//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[1]/a[3]').click()
    time.sleep(5)
    imgs = driver.find_element(By.XPATH, '//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a').get_attribute('href')
    imgLinks = []
    imgLinks.append(imgs)
    print(imgLinks)
    count +=1
    
