# Import the necessary modules
from requests_html import HTMLSession

# Open a file in write mode to store the scraped HTML content
file_path = 'scraped.html'
html_file = open(file_path, 'w', encoding='utf-8')

# Create an HTML session using requests_html library
session = HTMLSession()

# Send a GET request to the specified URL
r = session.get('https://www.naijaloaded.com.ng/download-music/wizkid-ft-tems-justin-bieber-essence-remix')

# Get the HTML content of the response
html_content = r.html.html

# Print the results on the terminal
# print(html_content)

# Write the HTML content to the file
html_file.write(html_content)

# Close the file after writing the HTML content
html_file.close()