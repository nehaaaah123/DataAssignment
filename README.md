# Web Scraping and Data Security Project Report

## 1. Description of the Website Scraped
We utilized [Books to Scrape](http://books.toscrape.com), a website specifically designed for practicing web scraping techniques. This website was chosen because:
- It's built for educational purposes and allows scraping
- Contains structured data about books
- Provides consistent data format
- Has multiple data points per item
- Offers reliable uptime and performance

## 2. Fields Extracted
From each book listing, we extracted the following data points:

| Field | Description | Example |
|-------|-------------|---------|
| Title | The complete book title | "The Great Gatsby" |
| Price | Book price in £ | "£9.99" |
| Availability | Stock status | "In stock" |
| Rating | Star rating (One to Five) | "Four" |

The data is structured in a CSV format for easy processing and analysis.

## 3. Security Approach Used
We implemented a robust security system using the following measures:

### A. Encryption Implementation
- Used Fernet symmetric encryption (from `cryptography` library)
- Generated secure encryption keys
- Implemented both encryption and decryption capabilities

```python
# Key Generation
key = Fernet.generate_key()
with open("secret.key", "wb") as key_file:
    key_file.write(key)

# Encryption
fernet = Fernet(key)
encrypted_data = fernet.encrypt(original_data)
```

### B. Data Protection Flow
1. Raw data saved as `books_raw.csv`
2. Data encrypted and saved as `books_encrypted.csv`
3. Encryption key stored separately as `secret.key`
4. Decryption verification with `books_decrypted.csv`

## 4. Challenges Faced

### Technical Challenges
1. **HTML Structure Navigation**
   - Solution: Used BeautifulSoup's class-based selectors
   - Implemented error handling for missing elements

2. **Data Consistency**
   - Challenge: Maintaining data integrity during encryption
   - Solution: Implemented verification through decryption testing

3. **File Handling**
   - Challenge: Managing multiple file operations
   - Solution: Used context managers (`with` statements) for safe file operations

### Implementation Challenges
1. **Security Implementation**
   - Challenge: Secure key management
   - Solution: Separated key storage from encrypted data

2. **Error Handling**
   - Challenge: Robust error handling for network issues
   - Solution: Implemented try-except blocks with specific exceptions

## 5. Code Snippets and Implementation

### Web Scraping Implementation
```python
# Extract book data
for book in soup.find_all("article", class_="product_pod"):
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text.strip()
    availability = book.find("p", class_="instock").text.strip()
    rating = book.find("p", class_="star-rating")["class"][1]
```

### Data Security Implementation
```python
# Encryption process
with open("books_raw.csv", "rb") as file:
    original_data = file.read()

fernet = Fernet(key)
encrypted_data = fernet.encrypt(original_data)

with open("books_encrypted.csv", "wb") as enc_file:
    enc_file.write(encrypted_data)
```

## 6. Ethical Considerations

### Implemented Practices
1. **Rate Limiting**
   - Added delays between requests (2 seconds)
   - Prevents server overload
   ```python
   time.sleep(2)  # delay between requests
   ```

2. **Proper Identification**
   - Used clear user-agent headers
   ```python
   headers = {"User-Agent": "Mozilla/5.0"}
   ```

3. **Data Protection**
   - Encrypted sensitive information
   - Secure key management
   - Protected stored data
