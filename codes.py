# import the file contain the import modules
import modules

# assigning the variable initialized in modules
driver = modules.driver
By = modules.By
time = modules.time

# to get the url of the website to be tested
driver.implicitly_wait(5)
print("Enter the website url to be tested \n")
url = str(input())
driver.get(url)

# to select the choice for perform the action
print("enter your choice to be performed ! \n")
print('\n1.find element and sent data\n2.drag and drop\n3.Click function\n4.image \n5.Navigate function \n6.exit')
ch = int(input("input enter the choice:\t"))
# from the selected choice we will execute the corresponding operation


if ch == 1 :
    print(
        "select the method to find element \n1.By.ID \n2.By Name \n3.By Xpath \n4.Tag name\n5.Link text\n6.css selector\n7.Class name\n8.exit")


# to select the options for choose the method to select the input function
def find_element() :
    options = int(input("enter the type"))

    # if the option is choose by id
    if options == 1 :
        print("enter the ID")
        value = str(input())
        driver.find_element(By.ID, value)
        print("enter the text to be inserted ")
        text = str(input())
        driver.send_keys(text)

    # if the option is choose by Name
    elif options == 2 :
        print("enter the Name")
        value = str(input())
        driver.find_element(By.NAME, value)
        print("enter the text to be inserted ")
        text = str(input())
        driver.send_keys(text)

    # if the option is choose by Xpath
    elif options == 3 :
        print("enter the Xpath")
        value = str(input())
        driver.find_element(By.XPATH, value)
        print("enter the text to be inserted ")
        text = str(input())
        driver.send_keys(text)

    # if the option is choose by Tag Name
    elif options == 4 :
        print("enter the Tag name")
        value = str(input())
        driver.find_element(By.TAG_NAME, value)
        print("enter the text to be inserted ")
        text = str(input())
        driver.send_keys(text)

    # if the option is choose by Link Text
    elif options == 5 :
        print("enter the Link Text")
        value = str(input())
        driver.find_element(By.LINK_TEXT, value)
        print("enter the text to be inserted ")
        text =str(input())
        driver.send_keys(text)

    # if the option is choose by CSS Selector
    elif options == 6 :
        print("enter the css selector")
        value = str(input())
        driver.find_element(By.CSS_SELECTOR, value)
        print("enter the text to be inserted ")
        text = str(input())
        driver.send_keys(text)

    # if the option is choose by Class name
    elif options == 7 :
        print("enter the class name")
        value = str(input())
        driver.find_element(By.CLASS_NAME, value)
        print("enter the text to be inserted ")
        text = str(input())
        driver.send_keys(text)

    elif options == 8 :
        exit(0)
    else :
        print("please choose a correct option")

    # if the user really want to repeat the process or not
    def repeat_again() :
        find_again = input("Do you want to calculate again? Please type Y for YES or N for NO.")
        if find_again.upper() == 'Y' :
            find_element()
        elif find_again.upper() == 'N' :
            print('See you later.')
        else :
            repeat_again()


find_element()

# The options for ch == 1 ends at the above line
# To perform drag and drop operations
if ch == 2 :
    print("enter the source id")
    source = str(input())
    driver.find_element_by_id(source)
    target = str(input())
    select = modules.Select(source)
    drop = select.options
    for element in drop :
        if element.text == target :
            element.click()
            break

# radio button also work if the locator we use xpath instead of id
# To perform the click Functions
if ch == 3 :
    print("enter the id for locate the button\n")
    button = str(input())
    driver.find_element(By.ID, 'button').click()

# To Fetch the image files
if ch == 4 :
    images = driver.find_elements_by_tag_name('img')
    for image in images :
        print(image.get_attribute('src'))

if ch == 5 :
    def navigation() :
        print("select the type of navigation should be performed")
        print("\n1.Forward \n2.Backward \n3.Refresh \n4.close window \n5.Close Browser \n6.exit")


    move = int(input())

    # To perform the forward function
    if move == 1 :
        driver.navigate().forward()
        time.sleep(4)

    # To perform the backward function
    elif move == 2 :
        driver.navigate().backward()
        time.sleep(4)

    # To perform the refresh function
    elif move == 3 :
        driver.navigate().refresh()
        time.sleep(4)

    # To perform the forward close windows
    elif move == 4 :
        driver.close()
        time.sleep(4)

    elif move == 5 :
        exit(0)

    else :
        print("enter a valid number")

# To close the browser
driver.quit()
time.sleep(4)
