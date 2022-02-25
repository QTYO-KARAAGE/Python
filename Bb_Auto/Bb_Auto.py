from re import search
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

print("実行中...")
chrome = webdriver.Chrome("./driver/chromedriver.exe")
print("...")
chrome.execute_script("window.op('','_blank');")
chrome.switch_to.window(chrome.window_handles[1])
print("...")
chrome.get("https://bb.kosen-ac.jp")

search_box = chrome.find_element_by_name("pattern")
search_words = ("沖縄工業高等専門学校")
search_box.send_keys(" ".join(search_words))

print("完了しました。")
input()