from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the WebDriver (Make sure to have the appropriate driver executable)
driver_path = r"/opt/homebrew/bin/chromedriver"  # Update this path if necessary
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# Define credentials
email = "likhithraju0@gmail.com"
wrong_password = "wrongpassword"
correct_password = "Likhithraju@79"

try:
    # Open Indiahikes homepage
    driver.get("https://indiahikes.com/")
    driver.maximize_window()
    time.sleep(5)

    # Click on "My Profile" to go to the login page
    my_profile_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'My Profile')]"))
    )
    my_profile_button.click()
    time.sleep(5)

    # Enter email and wrong password
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[4]/div[1]/div/div/div/div/div/div/form/div[1]/input"))
    )
    email_input = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[4]/div[1]/div/div/div/div/div/div/form/div[1]/input")
    email_input.send_keys(email)
    password_input = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[4]/div[1]/div/div/div/div/div/div/form/div[2]/input")
    password_input.send_keys(wrong_password)
    login_button = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[4]/div[1]/div/div/div/div/div/div/form/div[4]/input[2]")
    login_button.click()
    time.sleep(5)

    # Clear the fields and enter the correct password
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[4]/div[1]/div/div/div/div/div/div/form/div[1]/input"))
    )
    email_input = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[4]/div[1]/div/div/div/div/div/div/form/div[1]/input")
    email_input.clear()
    password_input = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[4]/div[1]/div/div/div/div/div/div/form/div[2]/input")
    password_input.clear()
    email_input.send_keys(email)
    password_input.send_keys(correct_password)
    login_button = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[4]/div[1]/div/div/div/div/div/div/form/div[4]/input[2]")
    login_button.click()
    time.sleep(5)
    print("Logged in!")

    # Wait until the "Visit Indiahikes website" button is present and click it
    visit_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/main/div[1]/nav/div[2]/ul/li[9]/a/button"))
    )
    visit_button.click()
    time.sleep(5)

    upcoming_treks = WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/main/header/div[1]/nav[2]/div/div/div/a[1]"))
    )
    upcoming_treks.click()
    time.sleep(5)

    scroll1 = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[3]/div/div[3]/div/div/div/div[2]/div/div/div/div")
    driver.execute_script("arguments[0].scrollIntoView();", scroll1)
    time.sleep(3)

    chanderkhani_trek = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/main/div[3]/div/div[3]/div/div/div/div[2]/div/div/div/div/div/div/div/button[1]"))
    )
    chanderkhani_trek.click()
    time.sleep(5)


    scroll2 = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[3]/div/div/div/div/div/div[3]/section/div/div[1]/section[1]/div[1]/div[2]/i")
    driver.execute_script("arguments[0].scrollIntoView();", scroll2)
    time.sleep(3)

    click_arrow = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/main/div[3]/div/div/div/div/div/div[3]/section/div/div[1]/section[1]/div[1]/div[2]/i"))
    )
    click_arrow.click()
    time.sleep(5)

    select_date = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/main/div[3]/div/div/div/div/div/div[3]/section/div/div[1]/section[1]/div[2]/div/div[5]/div/p"))
    )
    select_date.click()
    time.sleep(5)
    print("Chanderkhani Trek")

    scroll3 = driver.find_element(By.XPATH,"/html/body/div[1]/div/main/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[1]/div/div/label/input")
    driver.execute_script("arguments[0].scrollIntoView();", scroll3)
    time.sleep(3)

    print("Booking Started")
    checkbox = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/main/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[1]/div/div/label/input"))
    )
    checkbox.click()
    time.sleep(5)

    proceed = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/main/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[2]/div"))
    )
    proceed.click()
    time.sleep(5)

    scroll4 = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div/div/button")
    driver.execute_script("arguments[0].scrollIntoView();", scroll4)
    time.sleep(3)

    proceed2 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/main/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div/div/button"))
    )
    proceed2.click()
    time.sleep(5)

    understand = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div[3]/button"))
    )
    understand.click()
    time.sleep(5)
    print("Booking paused")

    search_bar = driver.find_element(By.XPATH,"/html/body/div[1]/div/main/header/div[1]/nav[1]/div/div/form/input")
    search_bar.send_keys("dayara")
    time.sleep(3)
    print("Search Performed")

    #Clicking on the Daya Bugyal Trek
    dayara = driver.find_element(By.XPATH,"/html/body/div[1]/div/main/header/div[1]/nav[1]/div/div/form/input")
    dayara.send_keys("dayara")
    time.sleep(3)

    dayara_click = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/main/div[1]/div[2]/div[1]/a/div/div/div[1]/div/span/img"))
    )
    dayara_click.click()
    print("Dayara Bugyal Trek Opened")

    shop = driver.find_element(By.XPATH,"/html/body/div[1]/div/main/header/div[1]/nav[1]/div/div/div/a[3]")
    shop.click()
    time.sleep(5)
    print("Shop Opened")

    trek_gear = driver.find_element(By.XPATH, "/html/body/div[3]/sticky-header/header/nav/ul/li[3]/a")
    trek_gear.click()
    time.sleep(5)

    bag_click = driver.find_element(By.XPATH, "/html/body/main/div/div/div/div/div/ul/li[3]/div/div/div[2]/div[1]/h3/a")
    bag_click.click()
    time.sleep(5)

    bag_cart = driver.find_element(By.XPATH,"/html/body/main/section[1]/section/div/div/div[3]/product-info/div[7]/product-form/form/div/button")
    bag_cart.click()
    time.sleep(5)

    close = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[2]/div/button")
    close.click()
    time.sleep(5)

    trek_gear_page = driver.find_element(By.XPATH, "/html/body/div[3]/sticky-header/header/nav/ul/li[3]/a")
    trek_gear_page.click()
    time.sleep(5)

    rain_coat = driver.find_element(By.XPATH,"/html/body/main/div/div/div/div/div/ul/li[7]/div/div")
    rain_coat.click()
    time.sleep(5)

    add = driver.find_element(By.XPATH,"/html/body/main/section[1]/section/div/div/div[3]/product-info/div[5]/div[1]/quantity-input/button[2]")
    add.click()
    time.sleep(5)

    cart = driver.find_element(By.XPATH,"/html/body/main/section[1]/section/div/div/div[3]/product-info/div[6]/product-form/form/div/button")
    cart.click()
    time.sleep(5)

    remove = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[2]/div/div[3]/div[1]/div[4]/div[3]/div[1]/div[2]/span")
    remove.click()
    time.sleep(5)

    checkout = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[2]/div/div[3]/div[3]/div[2]/div[2]/div[4]/button")
    checkout.click()
    time.sleep(5)
    print("CheckOut")


    print("Website Automated Successfully !")




finally:
    # Quit the driver
    time.sleep(5)
    driver.quit()
