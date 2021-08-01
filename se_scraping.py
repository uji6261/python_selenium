from selenium import webdriver
import selenium
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time


options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--disable-setuid-sandbox')
options.add_argument('--no-sandbox')
options.add_argument('--ignore-certificate-errors=true')
 
url = "https://www.next1step.com/category/python/scraping_sample_page/"
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.implicitly_wait(10)

driver.get(url)
print(driver.title)

# タグ指定：h2要素を取得する
elems = driver.find_elements_by_tag_name("h2")

for elem in elems:
    print(elem.text)

# class指定：
elems = driver.find_elements_by_class_name('ep-box')
elem = elems[0]
print(elem.text)

# liの取得
elems = driver.find_element_by_tag_name("article").find_elements_by_tag_name("li")

for elem in elems:
    print(elem.text)


# 画像をダウンロードする
# seliniumでは、画像の保存をスクリーンショットとして保存できる

# img_elem = driver.find_element_by_xpath("//img[@alt='へびせんせいのサンプル画像']") 完全一致はこちら
img_elem = driver.find_element_by_xpath("//img[contains(@alt,'サンプル画像')]")

with open("out.png", "wb") as f:
    f.write(img_elem.screenshot_as_png)

# テーブルの情報を取得する
elem = driver.find_element_by_tag_name('table')
tds = elem.find_elements_by_tag_name('td')

for i in range(int(len(tds)/2)):
    print(tds[i * 2].text + '  ' + tds[i * 2 + 1].text)

# テキストボックスに文字を入力し、ボタンを押す
name_elem = driver.find_element_by_name('name')
mail_elem = driver.find_element_by_name('mail')
button_elem = driver.find_element_by_xpath("//input[@value='確認する']")

driver.find_element_by_tag_name('body').send_keys(Keys.END)
time.sleep(1)
name_elem.send_keys('かばくん')
mail_elem.send_keys('kabakun@xxxxxx.xx')
button_elem.click()

# ブラウザの終了
time.sleep(5)
driver.quit()
