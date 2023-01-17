import requests
from bs4 import BeautifulSoup

#AUTHOR: Cameron Noakes
# This script sends a GET request to the target website, retrieves the HTML source code,
# and parses it using BeautifulSoup. It then extracts the website's title, meta tags,
# and links. With this information, you could analyze the website's meta tags to detect
# the technologies used, such as the web server, programming languages, and content
# management system (CMS (WordPress, Joomla, Drupal)).


# Use Case:
# This tool can be used for specific web application penetration testing engagements and other security assessments to gather
# recon information through somewhat passive enumeration means. This will help automate manual processes of PTs to be able
# to focus on other aspects of the assessments.

# Define the target URL
url = "https://testDomain.com"

# Send a GET request to the website and retrieve the HTML source code
response = requests.get(url)
html_content = response.content

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Extract the website's title
title = soup.find('title').text
print("Title:", title)

# Extract the website's meta tags
meta_tags = soup.find_all('meta')
for tag in meta_tags:
    print(tag)

# Extract all links on the website
links = soup.find_all('a')
for link in links:
    print(link.get('href'))



