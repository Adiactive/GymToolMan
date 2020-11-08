from splinter import Browser
import time
import schedule

def register(activity):
    username = 'my_username'
    password = 'my_pwd'

    dict = {'gym': 1, 'badminton': 2}

    # Start the driver in headless mode
    browser = Browser('chrome', headless=True)

    browser.visit('https://warrior.uwaterloo.ca/')

    # Browse the Facility Access Reservation categories
    browser.find_by_css('.Menu-Item').first.click()

    # Browse the CIF FITNESS CENTER program
    browser.find_by_css('.list-group-item')[dict[activity]].click()

    # Check login status
    if browser.is_element_present_by_text('Log In'):
        print("Login required!")
        browser.execute_script("showLogin();")

        # wait for dynamic content to load
        while not browser.find_by_id("modalLogin").first.visible:
            time.sleep(.1)
        browser.execute_script("showLocalLoginForm();")
        
        # Fill the username and password
        print("Filling in user info...")
        while not browser.find_by_name("Username").first.visible:
            time.sleep(.1)
        while(browser.find_by_name("Username").first.value == ''):
            browser.fill('Username', username)
            browser.fill('Password', password)
        
        # Submit and login
        browser.execute_script("submitLogin();")

    # Wait for login process to finish, then reload
    print("Logging in...")
    while browser.is_element_present_by_id("modalLogin"):
            time.sleep(.1)
    print("Login Successful!")
    browser.reload()

    # Register the latest reservation
    resv = browser.find_by_text("Register")
    resv.last.click()

    # Accept the waiver and checkout
    print("Signing the waiver...")
    while not browser.find_by_text("Accept Now").first.visible:
            time.sleep(.1)
    browser.find_by_text("Accept Now").first.click()
    for i in range(1, 9):
        browser.choose(f'CustomPrompts[{i}].CommonInput', 'False')
    browser.find_by_text("Add to Cart").first.click()
    browser.execute_script("Submit();")
    print("Registerd!")
    return

schedule.every().monday.at("15:00").do(register,"gym")
schedule.every().wednesday.at("15:00").do(register,"badminton")
schedule.every().thursday.at("15:00").do(register,"gym")
schedule.every().friday.at("15:00").do(register,"gym")
schedule.every().saturday.at("15:00").do(register,"gym")
schedule.every().sunday.at("16:00").do(register,"gym")

while True:
    schedule.run_pending()
    time.sleep(1)

# register("badminton")

