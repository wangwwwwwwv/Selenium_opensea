import datetime
from selenium import webdriver

from selenium.webdriver.chrome.options import Options
import csv
import os

PATH = "C:\\Users\\ASUS\\Desktop\\selenium_opensea\\"
today = datetime.date.today()
try:
    os.mkdir(PATH+ str(today))
except:
    a = input("alrady exist continue enter '1'")
    if a != '1':
        exit()
PATH = PATH + str(today) + "\\"


chrome_options = Options()

browser = webdriver.Chrome(options=chrome_options)
browser.maximize_window()
browser.get('https://opensea.io/rankings')
DATA_All = {}
while len(DATA_All) != 100:
    for i in range(0,100):
        name_xpath = '//*[@id="main"]/div/div[2]/div/div[3]/div[' + str(i) + "]/a/div[1]/div[3]/span/div"
        rank_xpath = '//*[@id="main"]/div/div[2]/div/div[3]/div[' + str(i) + "]/a/div[1]/div[1]/span/div"
        volume_xpath = '//*[@id="main"]/div/div[2]/div/div[3]/div[' + str(i) + "]/a/div[2]/div/span/div"

        which_money_path = '//*[@id="main"]/div/div[2]/div/div[3]/div['+ str(i) + ']/a/div[2]/div/div/button'

        Twentyfour_H_path = '//*[@id="main"]/div/div[2]/div/div[3]/div[' + str(i) + "]/a/div[3]/div/span/div"
        Twentyfour_H_path_2 = '//*[@id="main"]/div/div[2]/div/div[3]/div[' + str(i) + "]/a/div[3]/div/p"


        Seven_day_path = '//*[@id="main"]/div/div[2]/div/div[3]/div[' + str(i) + "]/a/div[4]/div/span/div"
        Seven_day_path_2 = '//*[@id="main"]/div/div[2]/div/div[3]/div[' + str(i) + "]/a/div[4]/div/p"

        floor_price_path = '//*[@id="main"]/div/div[2]/div/div[3]/div[' + str(i) + "]/a/div[5]/div/span/div"

        owner_path = '//*[@id="main"]/div/div[2]/div/div[3]/div[' + str(i) + "]/a/div[6]/p"

        items_path = '//*[@id="main"]/div/div[2]/div/div[3]/div[' + str(i) + "]/a/div[7]/p"

        url_path = '//*[@id="main"]/div/div[2]/div/div[3]/div[' + str(i) + ']/a'




        try:
            name = browser.find_element_by_xpath(name_xpath)
        except:
            continue
            # print(name.text)
        rank = browser.find_element_by_xpath(rank_xpath)
        if DATA_All.get(rank.text) != None:
            continue
        # print(rank.text)
        volume = browser.find_element_by_xpath(volume_xpath)
        # print(volume.text)
        try:
            Twentyfour_H = browser.find_element_by_xpath(Twentyfour_H_path)
        except:
            Twentyfour_H = browser.find_element_by_xpath(Twentyfour_H_path_2)

        # print(Twentyfour_H.text)
        try:
            Seven_day = browser.find_element_by_xpath(Seven_day_path)
        except:
            Seven_day = browser.find_element_by_xpath(Seven_day_path_2)

        which_money = browser.find_element_by_xpath(which_money_path).get_attribute('aria-label').split(' ') [0]

        # print(Seven_day.text)
        floor_price = browser.find_element_by_xpath(floor_price_path)
        # print(floor_price.text)
        owner = browser.find_element_by_xpath(owner_path)
        # print(owner.text)
        items = browser.find_element_by_xpath(items_path)
        # print(items.text)
        url = browser.find_element_by_xpath(url_path).get_attribute('href')


        print(len(DATA_All))
        # print(rank.text,name.text,volume.text,Twentyfour_H.text)#,Seven_day,floor_price,owner,items)
        DATA_All[rank.text] = [rank.text,name.text,volume.text + ' ' + which_money,Twentyfour_H.text,Seven_day.text,floor_price.text,owner.text,items.text,url]

    browser.execute_script("window.scrollBy(0,300)")
print(DATA_All)
rank_list = []

for j in DATA_All:
    rank_list.append(int(j))

rank_list.sort()
print(rank_list)
browser.implicitly_wait(20)


header = ['排名','名字','价格','24h','7day','最低价','拥有人数','数量','主页']
with open(PATH + 'today_nft.csv','w',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for j in range(0,len(DATA_All)):
        writer.writerow(DATA_All[str(j+1)])
    f.close()
