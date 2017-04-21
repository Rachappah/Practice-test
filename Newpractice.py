'''
Created on 21/04/2017

@author: Rachappa
'''
from selenium import webdriver
import time
if __name__ == '__main__':
    driver=webdriver.Firefox()
    driver.get("https://www.google.co.in/?gfe_rd=cr&ei=rNL5WJehFZPz8AfFmZXICQ")
    
    try:
        driver.find_element_by_id("lst-ib").send_keys("sachin images")
        driver.find_element_by_xpath(".//*[@id='_fZl']").click()
        time.sleep(6)
        #driver.execute_script("window.scrollTo(0,document.body.Scroll Height):")
        driver.find_element_by_xpath(".//*[@id='imagebox_bigimages']/g-section-with-header/div[2]/h3/a").click()
        time.sleep(6)
        driver.find_element_by_xpath(".//*[@id='rg_s']/div[3]/a/img").click()
        time.sleep(6)
        driver.find_element_by_xpath(".//*[@id='irc_ra']/div").click()
        print('Test pass:ID found')
    except Exception as e:
        print('Exception found,format',format(e))
        driver.quit()    
    
