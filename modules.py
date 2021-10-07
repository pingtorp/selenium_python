#import all the modules required for the process
#to initialise the webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import requests
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
#To download the corresponding web driver manager.


Browser = "chrome"
if Browser == "chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif Browser == "firefox":
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
elif Browser == "safari":
    driver = webdriver.safari()
else:
    print("please enter the correct name:")