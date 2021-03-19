from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import numpy as np
import csv
from time import sleep
from lxml import html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

name_list = []


def click(driver,elem):
    driver.execute_script("arguments[0].scrollIntoView(false);", elem)
    elem.click()

def login():
    # ブラウザーを起動
    url = "https://www.instagram.com/"
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    sleep(5)
    show = driver.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
    show.send_keys("")
    show = driver.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input") 
    show.send_keys("")
    show.submit()
    sleep(10)

    #ログイン情報の扱い選択
    chose = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/section/div/button")
    chose.click()
    sleep(5)

    #お知らせ機能の選択
    driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
    sleep(5)
    os = driver.find_element_by_xpath("//*[@id='react-root']/section/main/section/div[3]/div[2]/div[1]/a/div").click()
        
    sleep(2)
    for os in driver.find_elements_by_tag_name("a"):
        print(os.text)
        name_list.append(os.text)
    Column = ['モデル']
    df = pd.DataFrame(name_list,columns=Column)
    clean = df.replace({"基本データ":"","ヘルプ":"","プレス":"","API":"","求人":"","プライバシー":"","利用規約":"","所在地":"","人気アカウント":"","ハッシュタグ":""})
    clean['モデル'].replace('',np.nan,inplace=True)
    print("This is first test {}".format(clean))
    clean.dropna(subset=["モデル"],inplace=True)
    print(clean)
    # CSV ファイル出力
    clean.to_csv(r"モデル候補.csv",encoding='utf_8_sig')
    return df

cookies = login()
