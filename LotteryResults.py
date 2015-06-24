# -*- coding: utf-8 -*-
import urllib
import urllib2
from bs4 import BeautifulSoup
import sys
reload(sys)  
reload(sys)
sys.setdefaultencoding('utf-8')
reload(sys)  
u = 2
while u > 1:
    print("Welcome to the Lottery System")
    url = "http://www.dlb.lk/dlb/index.php?option=com_jmsitemap&view=sitemap&Itemid=53"
    url2 = "http://www.nlb.lk/lotteries.php"
    data = urllib2.urlopen(url)
    data2 = urllib2.urlopen(url2)
    soup = BeautifulSoup(data)
    soup2 = BeautifulSoup(data2)
    list1={}
    list2={}
    counta = 01
    lista = []
    #Development
    const = "http://www.dlb.lk"
    const2 = "http://www.nlb.lk/"
    lottery1 = soup.find("ul", {"class" : "resultrmenu_class"}).find_all("a")
    # print(lottery1)
    for a in lottery1:
        list1[str(a.text).replace("\n", "")] = str(const + str(a.get("href")))
     
    #National
    lottery2 = soup2.find_all("a", {"class" : "bodyText"})
    for b in lottery2:
        list1[str(b.text)] =  str(const2 + str(b.get("href")).replace("lot", "id").replace("info", "more"))
     
    for key in list1.keys():
        list2[str(counta)] = key
        counta=counta+1
         
    for loter in list2.keys():
        print(str(loter) + ") " + list2[loter])
     
    val = raw_input("Enter the index number : ")
    if (val == "e"):
        u = 0
    else:
        print("Enter the lottery draw number")
        ida = raw_input("Enter the id : ")
        ul = list1[list2[val]]
        val1 = ul.replace("http://www.nlb.lk/results-more.php?id=", "")
        if "nlb.lk" in ul:
            ul1="http://www.nlb.lk/" + "show-results.php?dno=" + ida + "&lott=" + val1
            data4 = urllib2.urlopen(ul1)
            soup4 = BeautifulSoup(data4)
            data_set = soup4.find("strong", {"class" : "bodyText-black"})
            number1 = soup4.find("table", {"class" : "lottery-numbers"}).find_all("td")
            print(str(data_set.text).replace(" ", ""))
            for a in number1:
                lista.append((str(a.text).replace(" ", "")))
            print("Winning Numbers are : " + str(lista).replace("n", "").replace("'", "").replace("[", "").replace("]", "").replace(",", "").replace("t", "").replace("\\", ""))
        else:
            data_set2 = urllib2.urlopen(ul)
            soup5 = BeautifulSoup(data_set2)
             
            number2 = soup5.find_all("tr", {"class" : "alt"})
            for l in number2:
                res = ("\n"+str((l.text)).replace("\n", "")).encode('utf-8').replace(u'┬á', "")
        #         print(res)
                if str(ida) in res:
                    print(res)
        raw_input("")
# data3 = urllib2.urlopen(ul)
# soup3 = BeautifulSoup(data3)

