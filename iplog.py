from selenium import webdriver
import socket
import logging

# Create a webdriver object for Chrome browser
driver = webdriver.Chrome()

# Create a logger object and a file handler for writing logs to a file
logger = logging.getLogger("IPLogger")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("ip_log.txt")
logger.addHandler(file_handler)

# Define a list of websites to visit and log
websites = ["https://www.google.com", "https://www.bing.com", "https://www.yahoo.com"]

# Loop through the websites
for website in websites:
    # Open the website in the browser using selenium
    driver.get(website)

    # Get the IP address of the website by passing its domain name using socket
    domain_name = website.split("//")[1]
    ip_address = socket.gethostbyname(domain_name)

    # Write the website name and IP address to the log file using logging
    logger.info(f"Website: {website}, IP: {ip_address}")
