import time
from selenium import webdriver
import pdfkit
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import telepot


config = {
    'EMAIL': '**',
    'PASSWORD': '**'
}

login_url = 'https://autentica.cpd.ua.es/cas/login?service=https://cvnet.cpd.ua.es/uacloud/home/indexVerificado'

def send_message():
    bot_token = '**'
    bot_chat_id = '**'

    bot = telepot.Bot(bot_token)
    
    bot.sendPhoto(bot_chat_id, photo=open('notas_TC.png', 'rb'))

def main():
    driver = webdriver.Chrome('path_to_chrome_driver')  # Optional argument, if not specified will search path.
    driver.get(login_url)
    elem = driver.find_element_by_xpath('/html/body/main/div/div/div/div[3]/div/div[1]/div/div[1]/div/form/div/div[3]/div[2]/input')
    elem.clear()
    elem.send_keys(config['EMAIL'])
    elem = driver.find_element_by_xpath('/html/body/main/div/div/div/div[3]/div/div[1]/div/div[1]/div/form/div/div[3]/div[3]/div/input')
    elem.clear()
    elem.send_keys(config['PASSWORD'])
    elem.send_keys(Keys.RETURN)
    driver.get("https://cvnet.cpd.ua.es/uaEvalua/miscontroles?pIdOpc=166")
    print('click')
    driver.find_element_by_xpath("/html/body/div[1]/form/div[3]/ul/li/select").click()
    print('no click')
    driver.find_element_by_xpath("/html/body/div[1]/form/div[3]/ul/li/select/option[4]").click()
    time.sleep(2)
    while True:
        time.sleep(2)
        notes_html = driver.find_element_by_xpath("/html/body/div[4]/div[3]/div[1]/div/ul/li[3]").get_attribute('innerHTML')
        notes_html = notes_html.replace(' ', '')
        
        for i in range(1, 6):
            if str(i) in notes_html:
                print('NOTAS!!')
                driver.refresh()
                time.sleep(5)
                driver.save_screenshot('notas_TC.png')
                send_message()
                driver.close()
            
            time.sleep(10)
            driver.refresh()

if __name__ == '__main__':
    main()
