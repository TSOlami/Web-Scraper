# A Simple Web-Scraper

This is a beginner-friendly guide to setting up and running a simple web-scraper written in Python. This guide assumes no prior knowledge of Python or web scraping.

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher

## Installation

1. **Install Python:**
   - Visit [Python's official website](https://www.python.org/downloads/) and download the latest version for Windows.
   - Run the installer. Ensure you check the box that says "Add Python 3.x to PATH" before clicking "Install Now".

2. **Verify Python Installation:**
   - Open your command prompt (search for `cmd` in the Start menu) and type:
     ```
     python --version
     ```
   - If the installation was successful, you should see the Python version number.

3. **Set Up a Virtual Environment (Optional but Recommended):**
   - In your command prompt, navigate to the folder where you want to store your project, then run:
     ```
     python -m venv myprojectenv
     ```
   - Activate the virtual environment:
     - On Windows:
       ```
       myprojectenv\Scripts\activate
       ```
     - On macOS and Linux:
       ```
       source myprojectenv/bin/activate
       ```

4. **Install Required Packages:**
   - Ensure your virtual environment is activated.
   - Install the necessary Python packages by running:
     ```
     pip install -r requirements.txt 
     ```

## Running the Script

1. **Download the Script:**
   - Download the web scraper script from the provided link or repository.

2. **Navigate to the Script's Directory:**
   - Use the command prompt to navigate to the directory where you downloaded the script. For example:
     ```
     cd path\to\your\script
     ```

3. **Run the Script:**
   - Execute the script by running:
     ```
     python scrape.py
     ```
   - The first prompt will ask you to enter a URL. This is the web page that the script will scrape.
   - The second prompt will ask you to enter the file name to save the scraped content as. This name will be used to create an HTML file containing the scraped data.

## Understanding the Output

- The script will scrape data from a specified web page and output the results. The exact nature of the output will depend on what the script is designed to scrape and how it's programmed to present this data.

## Troubleshooting

- If you encounter any errors, make sure Python and all required packages are correctly installed. Also, check that you're in the correct directory where the script is located.

Congratulations! You've just run your first web scraping script. Explore modifying the script to scrape different websites or data according to your needs.