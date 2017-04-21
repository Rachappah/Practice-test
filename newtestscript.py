'''
Created on 06/04/2017

@author: Rachappa
'''
from selenium import webdriver
import time

from select import select
from selenium.webdriver.support.select import Select
from _elementtree import Element
if __name__ == '__main__':
    driver=webdriver.Firefox()
    driver.get("http://www.airasia.com/in/en/home.page?cid=1")
#     
#     icon=driver.find_element_by_class_name("expand-icon")
#     icon.click()
#     driver.find_element_by_xpath("//li[text()='Bengaluru (BLR)']").click()
#     icon.click()
#     driver.find_element_by_xpath("li[text()='Hyderabad (HYD)']").click()
    
    #element=driver.find_element_by_xpath("//select[@id='adtPaxCount']")
    #element.click()
    #print (element)
    #time.sleep(2)
    #e1=driver.find_element_by_xpath("//option[@value='8']").click()
    element=driver.find_element_by_xpath(".//*[@id='adtPaxCount']").click()
    sele=Select(element)
    sele.select_by_value("2")
    #sele.select_by_visible_text("3 Adults")
    
    
    #     element=driver.find_element_by_xpath(".//*[@id='fromInput']")
#     element.clear()
#     element.send_keys("Bangalore")
#     element=driver.find_element_by_xpath(".//*[@id='toInput']")
#     element.clear()
#     element.send_keys("Bidar")
    #driver.find_element_by_xpath(".//*[@id='adtPaxCount']").click()
    #driver.find_element_by_xpath(".//*[@id='adtPaxCount']/option[5]/button").click()
#count = 0
#for o in select.options:
    #print(o.text)
    #if(count>1):
        #select.select_by_visible_text(o.text)
    #select.save_screenshot("phase%d.png"%count)
    #count+=1      
                    

    

