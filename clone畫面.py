# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
import re
import os
os.chdir('C://Users//user//Desktop//pic')


chrome_options = Options() # 實體化一個啟動參數
# --- 添加啟動參數 --- #
chrome_options.add_argument('--no-sandbox')  # 解決DevToolsActivePort文件不存在報告錯誤問題
chrome_options.add_argument("--disable-gpu")  # 禁止使用GPU硬件加速
chrome_options.add_argument('--headless')  # 無介面
chrome_options.add_argument('--disable-javascript')  # 禁用javascript
chrome_options.add_argument('blink-settings=imagesEnabled=false')  # 禁用下載圖片

current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time())) #取得時間

browser = webdriver.Chrome(options=chrome_options) # 調用本機的Chrome_browser
browser.set_window_size(1560, 1024) #視窗開啟大小
browser.get('http://www.17ce.com') # 請求頁面，要打開的browser
kw = browser.find_element_by_id("url") # 輸入欄位ID
su = browser.find_element_by_id("btn_wr") # 提交按鈕ID
pic_path = 'C://Users//user//Desktop//pic//'+ current_time+ '.png' 
kw.send_keys("www.baidu.com") # 欄位寫入監控網址
su.click() # 點提交按鈕
time.sleep(2) # 等待數據下載
browser.save_screenshot(pic_path)
browser.quit() # 關閉browser