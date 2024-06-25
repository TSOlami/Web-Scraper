#!/usr/bin/env python3
import os
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Prompt the user for a URL and file name
url = input("Please enter a URL: ")
file_name = input("Please enter the file name to save the scraped content as: ")

# Print a message
print("Your request is being processed, Please wait...")

def download_css(session, css_url):
    try:
        r = session.get(css_url)
        if r.status_code == 200:
            return r.text
        else:
            print(f"Failed to download CSS from {css_url}")
            return ""
    except Exception as e:
        print(f"An error occurred while downloading CSS from {css_url}: {e}")
        return ""

def scraper():
    # Create an HTML session using requests_html library
    session = HTMLSession()
    
    try:
        # Send a GET request to the specified URL
        r = session.get(url)
        print(".")

        # Get the HTML content of the response
        html_content = r.html.html
        print(".")

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find all link tags with rel="stylesheet"
        link_tags = soup.find_all('link', rel='stylesheet')

        # For each link tag, download the CSS and embed it in the HTML
        for link_tag in link_tags:
            css_url = link_tag['href']
            css_url = urljoin(url, css_url)  # Ensure the URL is absolute
            css_content = download_css(session, css_url)
            if css_content:
                style_tag = soup.new_tag('style')
                style_tag.string = css_content
                link_tag.replace_with(style_tag)
        
        # Write the modified HTML content to the file
        file_path = f'{file_name}.html'
        with open(file_path, 'w', encoding='utf-8') as html_file:
            html_file.write(str(soup))
        print(".")

        # Close the HTML file
        html_file.close()

        print(f"Scraping completed. HTML content saved to '{file_name}.html'.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Call the scraper function
scraper()
