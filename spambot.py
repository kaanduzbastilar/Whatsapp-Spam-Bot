from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

message = ("""\
ASCII Art
veya
Mesaj
""")

amount = 10
delay = 0.5
contact = "Kişinin Adı"

options = webdriver.ChromeOptions()
options.add_argument('user-data-dir=C:\\ChromeProfile')
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options) #executable_path="C:\\chromedriver.exe", options=options

driver.get('https://web.whatsapp.com/')

time.sleep(20)

name_list = []

# //*[@id="pane-side"]/div[1]/div/div/div[9] -- CTRL+SHIFT+I yapıp konsoldan mouse ikonuna tıklayıp, soldaki kişilerden birini seçtikten sonra konsoldaki seçilmiş kısmı xpath olarak kopyala.

# //*[@id="pane-side"]/div[1]/div/div/div[9]/div/div/div/div[2]/div[1]/div[1]/span -- üstte seçtiğimizin içindeki div'lerden birinde kişinin ismi geçeni xpath olarak kopyala.


for i in range(1, 15):
    info = driver.find_element(By.XPATH, f'//*[@id="pane-side"]/div[1]/div/div/div[{i}]' + '/div/div/div/div[2]/div[1]/div[1]/span')
    name_list.append(info.text)

to_click = name_list.index(contact) + 1

driver.find_element(By.XPATH, f'//*[@id="pane-side"]/div[1]/div/div/div[{to_click}]').click()

time.sleep(2)

# //*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1] -- sohbet kısmının xpath kopyası.

for i in range(amount):
    text_box = driver.find_element("xpath", f'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]')
    text_box.send_keys(message)
    text_box.send_keys(Keys.ENTER)
    time.sleep(delay)

#find_element("xpath" veya By.XPATH), By.XPATH için kütüphane eklemen lazım