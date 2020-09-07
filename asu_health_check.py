# Note: MAKE SURE YOU HAVE CHROME VERSION 85. THIS PROGRAM WILL NOT WORK OTHERWISE.
# Made by quart-z on github.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys # keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import date
import os
import platform










# Fields for the user to change. Only have to change on initial run.

########### ENTER FIELDS BELOW IN ORDER FOR PROGRAM TO RUN ###########
######################################################################

username = "" # Enter your ASURITE username between the " ", example - username = "bobjones1"
password = "" # Enter your ASURITE password between the " ", example - password = "password123"
setTime = 4 # Delay between loading webpages, increase this if you're getting errors, your internet is likely too slow

######################################################################
########### ENTER FIELDS ABOVE IN ORDER FOR PROGRAM TO RUN ###########














# Beginning of program
if os.platform == "Windows":
	driverPath = os.path.join(os.getcwd(), "chromedriver.exe")
else:
	driverPath = os.path.join(os.getcwd(), "chromedriver")
driver = webdriver.Chrome(driverPath) # finds chromedriver through path user entered
driver.get("https://www.asu.edu/healthcheck/preferences.html") # driver.go, simply goes to asu webpage

# Signs in to myasu

usernameInput = driver.find_element_by_name("username") # finds username via inspect element, in source code of website
passwordInput = driver.find_element_by_name("password") # finds password via inspect element, in source code of website
usernameInput.send_keys(username) # finds username field, inputs username into username field
passwordInput.send_keys(password) # finds password field, inputs password into password field

passwordInput.send_keys(Keys.RETURN) # enters password into field

print("Username and password entered successfully...") # print for user
time.sleep(setTime)

# Starts to submit health check

try:
	submitCheck = driver.find_element_by_xpath('//*[@id="healthCheckContainer"]/a') # finds element in xpath
	driver.execute_script("arguments[0].click();", submitCheck) # clicks on health check button hiding behind another element. Javascript must be used to click on it, since it is being covered

	print("Loading health check window...") # print for user
	time.sleep(setTime) # Increase number if your internet is too slow
	print("Window loaded successfully, entering symptoms...") # print for user


	# Enter iframe, which is pop-up window for health check
	iframe = driver.find_elements_by_tag_name("iframe") # finds the elements that are under the tag name iframe, i.e., finds the iframe element ID
	driver.switch_to.frame(iframe[0]) # switches to the first, and only iframe, the daily health check
	clickSymptom1 = (driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div[3]/div/div[2]/button[4]/span[1]').click())  # finds 'none' element in xpath, placed in between '' to seperate from "" in xpath
	submitSymptom1 = (driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div[3]/div/div[3]/button/span[1]').click()) # finds 'next' element in xpath, placed in between '' to seperate from "" in xpath


	print("Entered first symptoms successfully...") # print for user
	time.sleep(setTime) # Increase number if your internet is too slow
	print("Entering second round of symptoms...") # print for user


	clickSymptom2 = (driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div[3]/div/div[3]/button/span[1]').click()) # finds 'none' element in xpath, placed in between '' to seperate from "" in xpath
	submitSymptom2 = (driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div[3]/div/div[4]/button/span[1]').click()) # finds 'submit' element in xpath, placed in between '' to seperate from "" in xpath


	print("\nHealth check complete at " + str(date.today()) + "\nThanks for using my software! - quart-z") # Thank you (:
	time.sleep(5) # Don't adjust this
	driver.quit() # quits selenium driver

except Exception as e:
	print("The following exception occured: ") # prompt for user
	print(e) # prints exception
	print("Please try restarting the program, if internet is too slow try adjusting sleep arguments.") # Most likely reason you are getting an exception
	driver.quit() # quits browser

