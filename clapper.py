from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as ucdriver
import time

# a function to browse to a website which needs a sign-in 
#   using gmail
def browse(website, gmail_uid):

    # chrome options allow you to control browser settings
    options = webdriver.ChromeOptions()
    # if you don't want the browser popup, then add this
    # options.add_argument('--headless')

    # start up/open your web browser
    driver = ucdriver.Chrome(
        executable_path='chromedriver.exe', 
        chrome_options=options)

    # create helper class variables to implicitly wait and 
    #   step forward in our process
    wait = WebDriverWait(driver, 10)
    step_function = lambda x: wait.until(
        EC.element_to_be_clickable((By.XPATH, x)))

    
    # browse to desired website
    new_url = "https://medium.com/@Better-By-01/setting-up-tryhackme-vpn-f67ee024bf5d"
    
    driver.get(new_url)
    step_function(
        '//*[text()="Follow"]'
    ).click()
    step_function(
        '//*[text()="Sign in"]'
    ).click()
    step_function(
        '//*[text()="Sign in with Google"]'
    ).click()
    
    
    # browse to the gmail sign-in page
    driver.get("https://www.google.com/url?q=https://"
               "accounts.google.com/signin/v2/identifier%"
               "3Fec%3Dhpp_signin_001&source=hpp&id=19027"
               "682&ct=7&usg=AOvVaw1qUjFhPxp7fMYOATo9Y8zd")

    # add your gmail username/id in the text field, then 
    # click next button
    step_function(
        '//*[@id="identifierId"]'
    ).send_keys(gmail_uid)
    step_function(
        '//*[@id="identifierNext"]'
    ).click()

    # wait, and add gmail password to text field, then 
    # click next button
    driver.implicitly_wait(10)
    try:
        step_function(
            '//*[@id="password"]/div[1]/div/div[1]/input'
        ).send_keys('your_password')    # change to your password.
    except:
        pass
    try:
        step_function(
            '//*[@id="passwordNext"]/div/button/span'
        ).click()
    except:
        pass
    
    time.sleep(2)
    
    try:
        step_function(
            '//*[@id="password"]/div[1]/div/div[1]/input'
        ).send_keys('your_mail')  # change to your mailID
    except:
         pass
    try:
        step_function(
            '//*[@id="passwordNext"]/div/button/span'
        ).click()
    except:
        pass
    
       
    
    # login again in the medium page
  
    driver.get(new_url);

    time.sleep(2)
    
    try:
        step_function(
            '//*[text()="Follow"]'
        ).click()
    except:
        pass    
    
    step_function(
        '//*[text()="Sign in"]'
    ).click()
    
    step_function(
        '//*[text()="Sign in with Google"]'
    ).click()     
    

    # subscribe button
    try:
        step_function(
            '//*[text()="Follow"]'
        ).click()
    except:
        pass
    try:
        step_function(
            '//*[@id="root"]/div/div/div/div/main/div/div/div[1]/div/div/div/div[3]/div/div/div/div/button'
        ).click()
    except:
        pass

    try:
        step_function(
    	    '//*[@id="root"]/div/div/div/div/main/div/div/div[1]/div/div/div/div[3]/div/div/div/div/div/button'
        ).click()
    except:
        pass
    
    time.sleep(5)

    driver.get(new_url)
    
    # clapping button 
    
    for i in range(60):
        print(i)
        try:
            step_function(
                '//*[@id="root"]/div/div/div/div/main/div/div[2]/footer/div/div/div/div/div/div/span/div/div/div/div/div/button'
            ).click()
        except:
            pass

        try:
            step_function(
                '//*[@id="root"]/div/div/div/div/main/div/div[2]/footer/div/div/div/div/div/div/span[2]/div/div/div/div/div/button'
            ).click()
        except:
            pass 
        driver.implicitly_wait(20)	     

    time.sleep(2)
    driver.close()
  


website = 'https://accounts.google.com/o/oauth2/auth/identifier?operation=login&state=google-%7Chttps%3A%2F%2Fmedium.com%2F%3Fsource%3Dlogin--------------------------lo_home_nav-----------%7Clogin&access_type=online&client_id=216296035834-k1k6qe060s2tp2a2jam4ljdcms00sttg.apps.googleusercontent.com&redirect_uri=https%3A%2F%2Fmedium.com%2Fm%2Fcallback%2Fgoogle&response_type=id_token%20token&scope=email%20openid%20profile&nonce=1dea958c8d7b8fc989663a120f6503dec57c3cec4785434c4eaa9ba889576845&flowName=GeneralOAuthFlow'

with open('emails.txt') as f:
   emails = f.readlines()
   for email in emails:
       eml = email.split('\n')[0]
       browse(website, eml)
