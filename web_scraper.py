import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
 
# Step 1: Fetch the website
url ="http://books.toscrape.com"
headers = {"User-Agent": "Mozilla/5.0"}  # respectful request headers
 
try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # handle bad status codes
    time.sleep(2)  # delay between requests
except requests.exceptions.RequestException as e:
    print("❌ Error fetching the website:", e)
    exit()
 
# Step 2: Parse HTML
soup = BeautifulSoup(response.text, "html.parser")
 
# Step 3: Extract data
books_data = []
for book in soup.find_all("article", class_="product_pod"):
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text.strip()
    availability = book.find("p", class_="instock").text.strip()
    rating = book.find("p", class_="star-rating")["class"][1]
    
    books_data.append({
        "Title": title,
        "Price": price,
        "Availability": availability,
        "Rating": rating
    })
 
# Step 4: Store in CSV
df = pd.DataFrame(books_data)
df.to_csv("books_raw.csv", index=False)
print("✅ Raw data saved as 'books_raw.csv'")