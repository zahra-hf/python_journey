import requests
from bs4 import BeautifulSoup

url = "https://www.w3schools.com/html/html_images.asp"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract page title
    print("Page Title:")
    print(soup.title.text)

    # Extract information from a specific class
    headings = soup.find_all("h1")

    print("\nHeadings:")
    for h in headings:
        print(h.text)

    # Extract image links
    images = soup.find_all("img")

    print("\nImage Links:")
    for img in images:
        print(img.get("src"))

else:
    print("Connection Error")