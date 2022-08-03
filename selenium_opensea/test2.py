from asyncore import read
import datetime
import time
from selenium import webdriver

from selenium.webdriver.chrome.options import Options
import csv
import os
import requests
DATA_ALL = []
image_save_path = 'C:\\Users\\ASUS\\Desktop\\selenium_opensea\\2022-06-17\\image\\'

chrome_options = Options()

browser = webdriver.Chrome(options=chrome_options)
browser.maximize_window()

with open('C:\\Users\\ASUS\\Desktop\\selenium_opensea\\2022-06-17\\today_nft.csv','r') as f:
    reader = csv.reader(f)
    reader = list(reader)
    DATA_ALL.append(reader[0])
    f.close()

for j in range(1,len(reader)):
    each_line = reader[j]
    rank = reader[j][0]
    url = reader[j][-1]

    browser.get(url)
    image_url = []
    while len(image_url) < 2:
        for i in range(1,5):
            image_xpath = '//*[@id="main"]/div/div/div[5]/div/div[3]/div[3]/div[3]/div[3]/div[2]/div/div/div[' + str(i) + ']/div/article/a/div[1]/div/div/div/div/img'
            time.sleep(1)
            try:
                image_src = browser.find_element_by_xpath(image_xpath).get_attribute('src')
                print(image_src)
                if 'https' in image_src and image_src not in image_url:
                    image_url.append(image_src)
            except:
                browser.execute_script("window.scrollBy(0,900)")
        browser.execute_script("window.scrollBy(0,900)")
        

    for i in image_url:
        each_line.append(i)
    print(each_line)
    DATA_ALL.append(each_line)

    with open('test.csv','w',newline='') as f:
        writer = csv.writer(f)
        for j in DATA_ALL:
            writer.writerow(j)
    # for i in range(0,len(image_url)):
    #     image = requests.get(image_url[i])
    #     with open(rank+'_'+str(i) + '.png','wb') as f:
    #         f.write(image.content)
    #         f.close()
    


