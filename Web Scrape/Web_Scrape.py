import requests
from bs4 import BeautifulSoup

# Define website URL
website_url = "https://www.hackerone.com/"

# Send GET request and store response
response = requests.get(website_url)

# Check for successful response
if response.status_code == 200:
    # Parse HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract the title of the web page
    title = soup.find("title").text.strip()

    # Print the extracted title with proper formatting
    print(f"\nPage Title: {title}\n")

    # Extract all the heading elements of the page (h1, h2, h3, etc.)
    headings = soup.find_all("h[1-6]")

    # Print all the headings with their level
    print("Headings:")
    for heading in headings:
        print(f"{heading.name.upper()}: {heading.text.strip()}")

    # Extract the content of the first paragraph element
    paragraph = soup.find("p").text.strip()

    # Print the first paragraph
    print("\nFirst Paragraph:")
    print(paragraph)

else:
    print(f"Error: Could not access website. Status code: {response.status_code}")
