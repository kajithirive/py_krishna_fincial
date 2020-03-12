from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\\Users\\Dell\\ChromeWebdriver")

driver.get("http://localhost:5000/")

driver.find_element_by_name("click here to submit loan application form").click();

element = driver.find_element_by_name(“Your name”).sendkeys(“kaji”);
element = driver.find_element_by_name(“Your email”).sendkeys(“kajithiriveedhi00@gmail.com”);
element = driver.find_element_by_name(“Your age”).sendkeys(“24”);

element = driver.find_element_by_name("submit").click()

