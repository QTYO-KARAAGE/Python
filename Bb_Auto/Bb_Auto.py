from re import search
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#ブラウザ制御コメントの削除
#ChromeOptions = webdriver.ChromeOptions()
#ChromeOptions.add_experimental_option('excludeSwitches', ['enable-logging'])

print("実行中...")

#Chromeの起動
chrome = webdriver.Chrome("C:\\Users\\mi201315\\Desktop\\program\\Python\\Bb_Auto\\driver\\chromedriver.exe")
chrome.execute_script("window.open('','_blank');")
chrome.switch_to.window(chrome.window_handles[0])
chrome.get("https://bb.kosen-ac.jp")

print('実行中......')
#学校名入力
chrome.implicitly_wait(5)
search_box = chrome.find_element_by_name("pattern")
search_words = "沖縄工業高等専門学校"
search_box.send_keys("".join(search_words))

chrome.switch_to.window(chrome.window_handles[0])

print('実行中...')
#学校名を入力した後、「選択」をクリックする。
chrome.find_element_by_id('Login').click()

print("完了しました。")
