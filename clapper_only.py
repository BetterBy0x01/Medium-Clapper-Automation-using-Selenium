from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as ucdriver
import time
import sys

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
    wait = WebDriverWait(driver, 20)
    step_function = lambda x: wait.until(
        EC.element_to_be_clickable((By.XPATH, x)))

    
    # browse to desired website
    blog_url = sys.argv[1]
    
    driver.get(blog_url)
    step_function(
        '//*[text()="Sign In"]'
    ).click()
    step_function(
        '//*[text()="Sign in with Google"]'
    ).click()
    
    

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
    
    # password entry
    try:
        step_function(
            '//*[@id="password"]/div[1]/div/div[1]/input'
        ).send_keys('your_password')      # change the password to your gmail's password.
        
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
        ).send_keys('ap317151@gmail.com')
    except:
         pass
    try:
        step_function(
            '//*[@id="passwordNext"]/div/button/span'
        ).click()
    except:
        pass
    
    # Listen button
    #step_function(
    #    '//*[@id="root"]/div/div[3]/div/div/main/div/div[3]/div/div/article/div/div/header/div/div/div[2]/div[2]/div[4]/div/div/div/div/div/button'
    #).click()
    
    # clapping button 
    button1 = None
    button2 = None
    button3 = None
    button4 = None
    button5 = None
    clap_button = None
    
    print("HelloWorld1");       
    time.sleep(10)
    try:
        button1 = step_function(
            '//*[@id="root"]/div/div/div/div/main/div/div[3]/footer/div/div/div/div/div/div/span[2]/div/div/div/div/div/button'
        )
    except:
        print("button1 exception caught")
        time.sleep(300)
        pass
        
    
    print("HelloWorld2");        
    if button1 is not None:
        clap_button = button1
    elif button2 is not None:
        clap_button = button2
    elif button3 is not None:
        clap_button = button3
    elif button4 is not None:
        clap_button = button4 
    else:
        print("All params have value None")
        time.sleep(300)
        return
        driver.close() 

    print("HelloWorld3");        
    try:
        clap_button.click()
    except:
        print("clap_button clicking tried but exception occured")
        time.sleep(300)
    
    for i in range(55):
        print(i)
        clap_button.click()

    time.sleep(2)
    driver.close()
  


website = 'https://accounts.google.com/o/oauth2/auth/identifier?operation=login&state=google-%7Chttps%3A%2F%2Fmedium.com%2F%3Fsource%3Dlogin--------------------------lo_home_nav-----------%7Clogin&access_type=online&client_id=216296035834-k1k6qe060s2tp2a2jam4ljdcms00sttg.apps.googleusercontent.com&redirect_uri=https%3A%2F%2Fmedium.com%2Fm%2Fcallback%2Fgoogle&response_type=id_token%20token&scope=email%20openid%20profile&nonce=1dea958c8d7b8fc989663a120f6503dec57c3cec4785434c4eaa9ba889576845&flowName=GeneralOAuthFlow'

with open('clapper_emails.txt') as f:
   emails = f.readlines()
   for email in emails:
       eml = email.split('\n')[0]
       browse(website, eml)
