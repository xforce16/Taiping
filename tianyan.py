from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)


url = 'https://www.tianyancha.com/'
companyList=[]
usernames=["15310675140"]
passwords=['Taiping159']
ip_pool=[]
chromeOptions = webdriver.ChromeOptions()


def login():
    for proxy in ip_pool:
        chromeOptions.add_argument("--proxy-server={}").format(proxy)
        browser = webdriver.Chrome(chrome_options=chromeOptions)
        browser.get(url)
        index = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="nav-item nav-line"]/a[@class = "link-white"]')))
        index.click()
        browser.find_element_by_xpath("//div[text()='账号密码登录']").click()
        for user in usernames:
            browser.find_element_by_xpath("(//div[@class='pb30 position-rel']/input)[1]").send_keys(user)
            for password in passwords:
                browser.find_element_by_xpath("(//div[@class='pb40 position-rel']/input)[1]").send_keys(password)
                browser.find_element_by_xpath("//div[text()='登录']").click()
                print(browser.page_source)

def start_url():
    cookies = browser.get_cookies()


def run():
    login()

if __name__ == '__main__':
    run()


