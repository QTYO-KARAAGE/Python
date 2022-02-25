from re import search
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

print("実行中...")
chrome = webdriver.Chrome("C:\\Users\\mi201315\\Desktop\\program\\Python\\Bb_Auto\\driver\\chromedriver.exe")
print("...")
chrome.execute_script("window.open('','_blank');")
chrome.switch_to.window(chrome.window_handles[0])

chrome.get("https://bb.kosen-ac.jp")

#学校名入力
search_box = chrome.find_element_by_name("pattern")
search_words = "沖縄工業高等専門学校"
search_box.send_keys("".join(search_words))

chrome.switch_to.window(chrome.window_handles[0])

#学校名を入力した後、「選択」をクリックする。
chrome.execute_script('')

print("完了しました。")