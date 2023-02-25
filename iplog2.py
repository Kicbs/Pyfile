# Import the modules
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

# Define a loop condition
running = True

# Loop until the user quits
while running:
    # Ask the user to type a website inside the browser or quit
    input("Type a website inside the browser or type 'quit' to exit: ")

    # Check if the user typed 'quit'
    if driver.current_url == "quit":
        # Break out of the loop
        running = False
    else:
        # Get the current URL of the website using selenium current_url attribute[^1^][1] [^2^][2] [^3^][3] [^4^][4]
        website = driver.current_url

        # Get the IP address of the website by passing its domain name using socket
        domain_name = website.split("//")[1]
        ip_address = socket.gethostbyname(domain_name)

        # Write the website name and IP address to the log file using logging
        logger.info(f"Website: {website}, IP: {ip_address}")
