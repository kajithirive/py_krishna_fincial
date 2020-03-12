from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\\Users\\Dell\\ChromeWebdriver")

driver.get("http://localhost:5000/")

driver.find_element_by_name("click here to submit loan application form").click();

