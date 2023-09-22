#!/usr/bin/env python3
from requests_html import HTMLSession


# Prompt the user for a URL and file name
url: str = input("Please enter a url: ")
file_name: str = input(
		"Please enter the file name to save the scraped content as: ")

# Print a message
print("Your request is being processed, Please wait...")

def scraper()-> None:
	# Open a file in append mode to store the scraped HTML content
	file_path: str = f'{file_name}.html'
	html_file: str = open(file_path, 'a', encoding='utf-8')

	# Create an HTML session using requests_html library
	session = HTMLSession()

	try:
		# Send a GET request to the specified URL
		r = session.get(url)
		print(".")

		# Get the HTML content of the response
		html_content = r.html.html
		print(".")

		# Print the results on the terminal
		# print(html_content)

		# Write the HTML content to the file
		html_file.write(html_content)
		print(".")

		# Close the file after writing the HTML content
		html_file.close()

		print(f"Scraping completed. HTML content saved to '{file_name}.html'.")

	except Exception as e:
		print(f"An error occured: {e}")

# Call the scraper function
scraper()